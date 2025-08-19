// node login.js
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://leetcode.com/accounts/login/', { waitUntil: 'networkidle' });

  await page.fill('input[name="login"]', process.env.LEETCODE_USERNAME);
  await page.fill('input[name="password"]', process.env.LEETCODE_PASSWORD);
  await page.click('button[type="submit"]');

  // give time for post-login redirects
  await page.waitForNavigation({ waitUntil: 'networkidle', timeout: 15000 }).catch(()=>{});

  const cookies = await page.context().cookies();
  const session = cookies.find(c => c.name === 'LEETCODE_SESSION')?.value;
  const csrf = cookies.find(c => c.name === 'csrftoken')?.value;

  if (!session || !csrf) {
    console.error('Login failed or cookies not present.');
    process.exit(1);
  }

  // write to stdout or a file for the next steps to consume
  console.log(`LEETCODE_SESSION=${session}`);
  console.log(`LEETCODE_CSRF_TOKEN=${csrf}`);

  await browser.close();
})();
