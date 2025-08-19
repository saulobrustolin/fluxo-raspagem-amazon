import time

async def insert_text(page, brand):
    await page.fill("input[name='marca']", brand)
    time.sleep(1)
    return page