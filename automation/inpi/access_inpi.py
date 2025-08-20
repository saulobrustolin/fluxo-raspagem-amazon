from automation.steps.start import load_page
from automation.steps.navigate_section import navigate_section
from automation.steps.access_url_brand import access_url_brand
from automation.steps.insert_text import insert_text
from automation.steps.click_button_search import click_button_search
from automation.steps.verify_brand import verify_brand

from scripts.db.insert_brand import query_brand
from scripts.db.verify_in_database_brand import verify_in_database_brand

# async def access_inpi(ch, method, properties, body):
def access_inpi(brand):
    try:
        # try:
        #     brand = body.decode('utf-8', errors='ignore');
        # except:
        #     brand = body.decode('latin-1', errors='ignore');

        print(f'[access_inpi] Começando a fazer as verificações para "{brand}"')

        # antes de tudo: verificar se a marca já está registrada no banco de dados
        verify_in_db = verify_in_database_brand(brand)
        if verify_in_db == True:
            print(f'[brand] A marca {brand} está registrada no banco de dados como TRUE')
            return True
        if verify_in_db == False:
            print(f'[brand] A marca {brand} está registrada no banco de dados como FALSE')
            return False


        url = 'https://busca.inpi.gov.br/pePI/servlet/LoginController?action=login';
        condition = "img[src='/pePI/jsp/imagens/painel_servicos2_rgb.jpg']";

        playwright, browser, page = load_page(url, condition, headless=True)

        # step 1: access brand section
        navigate_section(page)
        # step 2: access url brand
        access_url_brand(page)
        # step 3: insert text in input
        insert_text(page, brand)
        # step 4: search
        click_button_search(page)
        # step 5: verify if is registred
        isRegistred = verify_brand(page)

        # fechando o navegador
        page.close()
        browser.close()

        # salva no banco de dados
        query_brand(brand, isRegistred)

        if isRegistred == False:
            print(f'[brand] A marca NÃO está registrada - {brand}')
            return False
        else:
            print(f'[brand] A marca ESTÁ registrada - {brand}')
            return True

    except Exception as e:
        print(f"[brand] Estou caindo em exception: {e}")
        return True
    