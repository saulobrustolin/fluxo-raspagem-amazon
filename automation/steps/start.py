from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

async def init_browser(headless=True):
    playwright = await async_playwright().start()
    browser = await playwright.chromium.launch(
        headless=headless,
        args=["--window-size=1366,768"]
    )
    return playwright, browser

async def load_page(url, condition, headless=True):
    playwright, browser = await init_browser(headless)
    page = await browser.new_page(viewport={"width": 1366, "height": 768})

    # abre a página
    await page.goto(url)

    # espera o seletor aparecer
    await page.wait_for_selector(condition, timeout=5000)

    return playwright, browser, page  # retorna a page para interações posteriores