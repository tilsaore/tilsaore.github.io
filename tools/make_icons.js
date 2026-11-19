// Render the site icons (browser tab, iPhone/Android home screen) from a "TO" monogram.
// Usage (from the repository root):  node tools/make_icons.js   then   python3 tools/make_favicon_ico.py
// Output: icons/icon-512.png, icon-192.png, apple-touch-icon.png (180), favicon-48/32/16.png
const path = require("path");
const { chromium } = require("playwright");

const RICE_BLUE = "#00205B";
const html = (size, rounded) => `<!doctype html><html><head>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@700&display=swap" rel="stylesheet">
<style>
  html, body { margin: 0; width: ${size}px; height: ${size}px; background: transparent; }
  .m { width: ${size}px; height: ${size}px; background: ${RICE_BLUE}; color: #fff;
       border-radius: ${rounded ? Math.round(size * 0.18) : 0}px;
       display: flex; align-items: center; justify-content: center;
       font: 700 ${Math.round(size * 0.5)}px/1 "Source Sans 3", sans-serif; letter-spacing: ${(-size * 0.01).toFixed(1)}px; }
</style></head><body><div class="m">TO</div></body></html>`;

(async () => {
  const root = path.resolve(__dirname, "..");
  const browser = await chromium.launch();
  // Rounded corners for browser tabs; full square for iOS/Android, which apply their own mask.
  const outputs = [
    ["icons/favicon-16.png", 16, true], ["icons/favicon-32.png", 32, true], ["icons/favicon-48.png", 48, true],
    ["icons/apple-touch-icon.png", 180, false], ["icons/icon-192.png", 192, false], ["icons/icon-512.png", 512, false],
  ];
  for (const [file, size, rounded] of outputs) {
    // Render large and let the browser downscale for crisp small sizes.
    const scale = size < 64 ? 8 : 1;
    const page = await browser.newPage({ viewport: { width: size, height: size }, deviceScaleFactor: scale });
    await page.setContent(html(size, rounded), { waitUntil: "networkidle" });
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.join(root, file), omitBackground: true });
    await page.close();
    console.log("wrote", file);
  }
  await browser.close();
})();
