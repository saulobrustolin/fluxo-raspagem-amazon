from automation.steps.start import load_page
from automation.steps.navigate_section import navigate_section
from automation.steps.access_url_brand import access_url_brand
from automation.steps.insert_text import insert_text
from automation.steps.click_button_search import click_button_search
from automation.steps.verify_brand import verify_brand

async def access_inpi(ch, method, properties, body):
    while True:
        try:
            brand = body.decode();
            print(f"inicializando análise na marca {brand}")

            url = 'https://busca.inpi.gov.br/pePI/servlet/LoginController?action=login';
            condition = "img[src='/pePI/jsp/imagens/painel_servicos2_rgb.jpg']";

            playwright, browser, page = await load_page(url, condition, headless=True)

            # step 1: access brand section
            await navigate_section(page)
            # step 2: access url brand
            await access_url_brand(page)
            # step 3: insert text in input
            await insert_text(page, brand)
            # step 4: search
            await click_button_search(page)
            # step 5: verify if is registred
            isRegistred = await verify_brand(page)
            # fechando o navegador
            await page.close()
            await browser.close()

            if isRegistred == False:
                print(f'[brand] A marca NÃO está registrada - {brand}')
                return False
            else:
                print(f'[brand] A marca ESTÁ registrada - {brand}')
                return True
        except:
            continue
    