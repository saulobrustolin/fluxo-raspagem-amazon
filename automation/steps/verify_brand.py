async def verify_brand(page):
    try:
        count = await page.locator("input[name='Action'][value='cadastroProcesso']").count()
        if count > 0:
            return False
        return True
    except:
        return True