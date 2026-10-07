// Renders dilemma carousels (cover + dilemma slide) from the bank in page.html.
// Usage: NODE_PATH=/opt/npm-tools/node_modules node tools/render.js <outDir> <picks.json>
// picks.json: [{"name":"d001","n":2,"hook":"WHO WINS?"}, ...]  (hook = exact English hook in the bank)
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
const [outDir, picksFile] = process.argv.slice(2);
if (!outDir || !picksFile) { console.error('usage: node render.js <outDir> <picks.json>'); process.exit(2); }
const picks = JSON.parse(fs.readFileSync(picksFile, 'utf8'));
const page = fs.readFileSync(path.join(__dirname, 'page.html'), 'utf8');
// Order of each n-choice list in the bank, as the page shows it.
const order = {};
for (const m of page.matchAll(/^D\((\d),'\w+',\["((?:[^"\\]|\\.)*)"/gm)) (order[m[1]] = order[m[1]] || []).push(m[2]);
for (const p of picks) {
  p.idx = (order[p.n] || []).indexOf(p.hook);
  if (p.idx < 0) { console.error('hook not found in bank for n=' + p.n + ': ' + p.hook); process.exit(1); }
}
fs.mkdirSync(outDir, { recursive: true });
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 400, height: 860 } });
  await pg.goto('file://' + path.join(__dirname, 'page.html')); await pg.waitForTimeout(1500);
  const res = await pg.evaluate(async (picks) => {
    const wait = () => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
    await document.fonts.load('80px Anton'); await document.fonts.ready;
    const q = s => document.querySelector(s), cv = q('#cv'), out = [], info = [];
    q('#seg-lang button[data-lang="en"]').click(); q('#presets button[data-p="0"]').click();
    q('#f-handle').value = '@blueredmemes'; q('#f-handle').dispatchEvent(new Event('input'));
    const cols = Math.min(10, picks.length), rows = Math.ceil(picks.length / cols);
    const sheet = document.createElement('canvas'); sheet.width = cols * 300; sheet.height = rows * 600; const c = sheet.getContext('2d');
    for (let k = 0; k < picks.length; k++) {
      q('#seg-n button[data-n="' + picks[k].n + '"]').click(); document.querySelectorAll('#bank button[data-j]')[picks[k].idx].click();
      for (let t = 0; t < (k + 2) % 5; t++) q('#btn-title').click();
      q('#seg-slide button[data-slide="cover"]').click(); await wait();
      out.push(cv.toDataURL('image/jpeg', 0.93)); c.drawImage(cv, (k % cols) * 300, Math.floor(k / cols) * 600, 300, 300);
      q('#seg-slide button[data-slide="main"]').click(); await wait();
      out.push(cv.toDataURL('image/jpeg', 0.93)); c.drawImage(cv, (k % cols) * 300, Math.floor(k / cols) * 600 + 300, 300, 300);
      info.push({ name: picks[k].name, n: picks[k].n, hook: q('#f-hook').value, tag: q('#f-tag').value, size: cv.width + 'x' + cv.height });
    }
    return { out, info, sheet: sheet.toDataURL('image/jpeg', 0.85) };
  }, picks);
  res.out.forEach((u, i) => fs.writeFileSync(path.join(outDir, `${picks[Math.floor(i / 2)].name}-${i % 2 ? '2-dilemma' : '1-cover'}.jpg`), Buffer.from(u.split(',')[1], 'base64')));
  fs.writeFileSync(path.join(outDir, 'sheet.jpg'), Buffer.from(res.sheet.split(',')[1], 'base64'));
  for (const x of res.info) { if (x.hook !== picks.find(p => p.name === x.name).hook) { console.error('MISMATCH for ' + x.name + ': rendered ' + x.hook); process.exitCode = 1; } }
  console.log(JSON.stringify(res.info)); await b.close();
})();
