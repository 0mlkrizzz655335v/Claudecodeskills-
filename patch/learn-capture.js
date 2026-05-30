#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

function getStore() {
  try {
    const distPath = path.join(__dirname, '..', 'dist', 'db', 'store.js');
    if (fs.existsSync(distPath)) {
      const mod = require(distPath);
      if (typeof mod.createStore === 'function') {
        return mod.createStore();
      }
    }
  } catch (e) {
    // better-sqlite3 native module not available, fallback to file mode
  }
  return null;
}

async function main() {
  let data = '';
  process.stdin.on('data', chunk => { data += chunk; });
  process.stdin.on('end', () => {
    try {
      const input = JSON.parse(data);
      const response = input.assistant_response || '';
      if (!response) {
        console.log(data);
        return;
      }

      const regex = /\[LEARN\]\s*([\w][\w\s-]*?)\s*:\s*(.+?)(?:\nMistake:\s*(.+?))?(?:\nCorrection:\s*(.+?))?(?:\nWiki:\s*([A-Za-z0-9_-]+))?(?=\n\[LEARN\]|\n\n|$)/gim;

      let match;
      let store = null;
      let count = 0;
      let lastIndex = -1;

      while ((match = regex.exec(response)) !== null) {
        if (regex.lastIndex === lastIndex) break;
        lastIndex = regex.lastIndex;

        if (!store) store = getStore();

        const projectDir = process.env.CLAUDE_PROJECT_DIR || '';
        const wikiSlug = match[5]?.trim() || undefined;
        const learning = {
          project: projectDir ? path.basename(projectDir) : null,
          category: match[1].trim(),
          rule: match[2].trim(),
          mistake: match[3]?.trim() || null,
          correction: match[4]?.trim() || null,
        };

        if (store) {
          store.addLearning(learning, wikiSlug);
        } else {
          // Fallback: write directly to LEARNED.md when DB is unavailable
          try {
            const learnedFile = path.join(process.env.HOME || process.env.USERPROFILE || '.', '.claude', 'LEARNED.md');
            const entry = `\n[LEARN] ${learning.category}: ${learning.rule}\nMistake: ${learning.mistake || 'N/A'}\nCorrection: ${learning.correction || 'N/A'}\n`;
            fs.appendFileSync(learnedFile, entry, 'utf8');
          } catch (e) {
            // Silent fallback failure
          }
        }
        count++;
      }

      if (count > 0) {
        console.error(`[ProWorkflow] Auto-saved ${count} learning(s) to database`);
      }
      if (store) store.close();
    } catch (err) {
      console.error(`[ProWorkflow] Learn-capture error: ${err.message}`);
    }
    console.log(data);
  });
}

main().catch(() => process.exit(0));
