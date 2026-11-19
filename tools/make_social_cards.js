// Render the link-preview cards (WhatsApp, LinkedIn, Slack, iMessage...) from tools/social-card.html.
// Usage (from the repository root):  node tools/make_social_cards.js
// Output: images/social-card.jpg, images/social-card-es.jpg, images/social-card-pt.jpg (1200x630)
const path = require("path");
const { chromium } = require("playwright");

(async () => {
  const root = path.resolve(__dirname, "..");
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
  for (const lang of ["en", "es", "pt"]) {
    await page.goto(`file://${root}/tools/social-card.html?lang=${lang}`, { waitUntil: "networkidle" });
    await page.evaluate(() => document.fonts.ready);
    const out = `images/social-card${lang === "en" ? "" : "-" + lang}.jpg`;
    await page.screenshot({ path: path.join(root, out), type: "jpeg", quality: 88 });
    console.log("wrote", out);
  }
  await browser.close();
})();
