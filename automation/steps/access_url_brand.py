import time

async def access_url_brand(page):
    await page.goto('https://busca.inpi.gov.br/pePI/jsp/marcas/Pesquisa_classe_basica.jsp');
    time.sleep(1)
    return page