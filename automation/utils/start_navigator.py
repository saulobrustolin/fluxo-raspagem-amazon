from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
from automation.utils.solve_captcha import solve_captcha

async def init_browser(headless=True):
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(headless=headless, args=["--window-size=1366,768"])
    return playwright, browser

async def start(url, condition):
    playwright, browser = await init_browser()
    page = await browser.new_page()
    await page.goto(url)
    try:
        await page.wait_for_selector(condition, timeout=5000)
    except:
        print('\n[page] Retornou uma página diferente da pretendida')
        # aqui você pode chamar uma versão async do solve_captcha
        solve = await solve_captcha(page)
        return solve
    html = await page.content()
    await page.close()
    await browser.close()
    await playwright.stop()
    return BeautifulSoup(html, "html.parser")
