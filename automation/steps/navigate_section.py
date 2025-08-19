import time

async def navigate_section(page):
    # 475 (x)
    # 200 (y)
    await page.mouse.click(475, 200);

    time.sleep(1)
    return page