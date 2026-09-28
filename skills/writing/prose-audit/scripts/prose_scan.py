#!/usr/bin/env python3
"""Read-only editorial cues and numeric surface comparison; not AI detection."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys


RULES = [
    ('opening', r'在当今.{0,12}时代|随着.{0,18}(?:快速|飞速|不断)发展', '检查开场是否提供必要背景。'),
    ('empty-importance', r'具有(?:十分|非常|极其)?重要意义|开启.{0,8}新篇章|注入新动(?:力|能)', '检查价值判断有无具体依据。'),
    ('announcement', r'值得注意的是|不难发现|让我们(?:一起)?深入探讨|接下来.{0,8}探讨', '可否直接给出所提示的信息？'),
    ('vague-source', r'专家(?:认为|指出)|研究表明|研究显示|行业报告显示', '检查附近是否给出真实来源；命中不等于无来源。'),
    ('nominalization', r'进行一个|实现对.{1,16}的|得以实现', '检查能否用原有动词写清动作。'),
    ('contrast', r'不仅.{1,50}(?:而且|更)|不是.{1,50}而是', '保留实质区别，只复核装饰性反转。'),
    ('canned-close', r'综上所述|未来可期|让我们共同期待|命运的齿轮', '检查是否真正完成本篇问题或场景。'),
    ('assistant-leak', r'作为(?:一个|一名)?AI|希望这对[你您]有帮助|如果[你您]需要.{0,16}我可以', '检查是否为误入成稿的助手交付语言。'),
    ('english-filler', r'\b(?:it is worth noting that|in today.s rapidly evolving|let.s dive into|a testament to)\b', 'Review whether the phrase adds information.'),
]
NUMBER = re.compile(r'(?<![A-Za-z0-9_])[-+−]?\d+(?:,\d{3})*(?:\.\d+)?(?:[eE][-+]?\d+)?(?:[%％])?')


def blank(match):
    return re.sub(r'[^\n]', ' ', match.group(0))


def mask(text, mask_quotes):
    """Keep line and column offsets while masking common protected spans."""
    lines = text.splitlines(keepends=True)
    if lines and lines[0].strip() == '---':
        end = next((i for i in range(1, len(lines)) if lines[i].strip() in ('---', '...')), None)
        if end is not None:
            for i in range(end + 1):
                lines[i] = re.sub(r'[^\n]', ' ', lines[i])
    fence = None
    for i, line in enumerate(lines):
        if fence:
            closing = re.match(r'^ {0,3}(' + re.escape(fence[0]) + r'{' + str(fence[1]) + r',})\s*$', line)
            lines[i] = re.sub(r'[^\n]', ' ', line)
            if closing:
                fence = None
            continue
        opening = re.match(r'^ {0,3}(`{3,}|~{3,})', line)
        if opening:
            marker = opening.group(1)
            fence = (marker[0], len(marker))
            lines[i] = re.sub(r'[^\n]', ' ', line)
        elif mask_quotes and re.match(r'^\s*>', line):
            lines[i] = re.sub(r'[^\n]', ' ', line)
    result = ''.join(lines)
    result = re.sub(r'(?<!`)(`+)([^`\n]*?)\1(?!`)', blank, result)
    result = re.sub(r'https?://[^\s<>\]\)]+', blank, result)
    if mask_quotes:
        for pattern in [r'“[^”]*”', r'「[^」]*」', r'『[^』]*』', r'"[^"\n]*"']:
            result = re.sub(pattern, blank, result)
    return result


def position(text, offset):
    return {'line': text.count('\n', 0, offset) + 1,
            'column': offset - text.rfind('\n', 0, offset)}


def scan(text):
    visible = mask(text, mask_quotes=True)
    cues = []
    for kind, pattern, note in RULES:
        for hit in re.finditer(pattern, visible, flags=re.I):
            cues.append({'kind': kind, **position(text, hit.start()),
                         'excerpt': text[hit.start():hit.end()], 'note': note})
    # Exact repeated paragraphs, retaining positions in the original source.
    seen = {}
    for block in re.finditer(r'\S[\s\S]*?(?=\n[ \t]*\n|\Z)', visible):
        normalized = re.sub(r'\s+', ' ', block.group()).strip()
        if len(normalized) < 20:
            continue
        if normalized in seen:
            cues.append({'kind': 'repeated-paragraph', **position(text, block.start()),
                         'excerpt': text[block.start():block.end()][:120],
                         'note': '与第 ' + str(seen[normalized]) + ' 行段落字面重复；检查是否必要。'})
        else:
            seen[normalized] = position(text, block.start())['line']
    cues.sort(key=lambda item: (item['line'], item['column'], item['kind']))
    return {'kind': 'editorial-cues', 'cues': cues,
            'note': '只读启发式定位，不判断作者或 AI 概率；零命中也不代表质量通过。'}


def numeric_inventory(text):
    # Quotes stay visible here because their numbers must also be protected.
    visible = mask(text, mask_quotes=False)
    result = []
    for hit in NUMBER.finditer(visible):
        left = text.rfind('\n', 0, hit.start()) + 1
        right = text.find('\n', hit.end())
        if right < 0:
            right = len(text)
        result.append({'value': hit.group(), **position(text, hit.start()),
                       'context': text[max(left, hit.start() - 35):min(right, hit.end() + 45)]})
    return result


def compare(before, after):
    old, new = numeric_inventory(before), numeric_inventory(after)
    old_count = Counter(item['value'] for item in old)
    new_count = Counter(item['value'] for item in new)
    return {'kind': 'numeric-surface-comparison',
            'removed_or_reduced': dict(old_count - new_count),
            'added_or_increased': dict(new_count - old_count),
            'before': old, 'after': new,
            'semantic_check_required': True,
            'note': '数字词面相同仍须人工检查对象、单位、否定、条件和因果；不检查代码块及元数据。'}


def read(path):
    return Path(path).read_text(encoding='utf-8-sig')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', nargs='?', help='UTF-8 plain text or Markdown to scan')
    parser.add_argument('--compare', nargs=2, metavar=('BEFORE', 'AFTER'), help='compare numeric surfaces; does not prove semantic equivalence')
    args = parser.parse_args()
    if bool(args.file) == bool(args.compare):
        parser.error('provide either one file or --compare BEFORE AFTER')
    try:
        result = compare(*(read(path) for path in args.compare)) if args.compare else scan(read(args.file))
    except (OSError, UnicodeError) as exc:
        print('Cannot read input: ' + str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
