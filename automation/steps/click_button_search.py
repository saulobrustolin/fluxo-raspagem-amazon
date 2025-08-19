import time

async def click_button_search(page):
    await page.click("input[name='botao']", force=True)
    time.sleep(1)
    return page