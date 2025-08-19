from automation.steps.start import load_page
from automation.steps.navigate_section import navigate_section
from automation.steps.access_url_brand import access_url_brand
from automation.steps.insert_text import insert_text
from automation.steps.click_button_search import click_button_search
from automation.steps.verify_brand import verify_brand

from scripts.db.insert_brand import query_brand

async def access_inpi(ch, method, properties, body):
    try:
        try:
            brand = body.decode('utf-8', errors='ignore');
        except:
            brand = body.decode('latin-1', errors='ignore');

        # antes de tudo: verificar se a marca já está registrada no banco de dados
        
        print(f'Começando a fazer as verificações para "{brand}"')

        url = 'https://busca.inpi.gov.br/pePI/servlet/LoginController?action=login';
        condition = "img[src='/pePI/jsp/imagens/painel_servicos2_rgb.jpg']";

        playwright, browser, page = await load_page(url, condition, headless=True)

        # step 1: access brand section
        await navigate_section(page)
        # step 2: access url brand
        await access_url_brand(page)
        # step 3: insert text in input
        await insert_text(page, brand)
        return
        # step 4: search
        await click_button_search(page)
        # step 5: verify if is registred
        isRegistred = await verify_brand(page)

        # salva no banco de dados
        # query_brand(brand, isRegistred)

        if isRegistred == False:
            print(f'[brand] A marca NÃO está registrada - {brand}')
            return False
        else:
            print(f'[brand] A marca ESTÁ registrada - {brand}')
            return True

    except Exception as e:
        print(f"[brand] Estou caindo em exception: {e}")
        return True
    finally:
        # fechando o navegador
        await page.close()
        await browser.close()
    
    