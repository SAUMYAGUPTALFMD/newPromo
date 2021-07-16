// const puppeteer = require('puppeteer');
const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({
        headless: false,
	});
	const page = await browser.newPage();
	const navigationPromise = page.waitForNavigation({waitUntil: "domcontentloaded"});
	await page.goto('https://ipindiaonline.gov.in/tmrpublicsearch/frmmain.aspx');
	await navigationPromise;

	// const next = await page.waitForSelector('#btnviewdetails');
	// await next.click();

	// console.log('Waiting for input to be ready.');
	// await page.waitForSelector('input');
	// console.log('Input is ready...');
	await page.selectOption('select#ContentPlaceHolder1_DDLFilter', 'Contains');
	// await page.select('#ContentPlaceHolder1_DDLFilter', 'Contains')
	await page.focus('#ContentPlaceHolder1_TBWordmark')
	page.keyboard.type('Sun')

	// await page.focus('#ContentPlaceHolder1_TBWordmark')
	await page.focus('#ContentPlaceHolder1_TBClass')
	page.keyboard.type(5)

	await page.focus('#ContentPlaceHolder1_BtnSearch')
	const searchButtonNodeSelector = "#ContentPlaceHolder1_BtnSearch";
	await page.click(searchButtonNodeSelector);
})();

