from config.start_navigator import start
from scripts.product.number_offers import number_offers
from scripts.product.avaliable import get_avaliable
from scripts.product.brand import get_brand
from config.start_navigator import init_browser

def scrapping(ch, method, properties, body):
    url = body.decode();

    # processo de inicialização
    init_browser(headless=False);
    
    condition = 'div[id="dynamic-aod-ingress-box"]';

    soup = start(url, condition);

    # print url
    print("URL:", url);

    # lógica para capturar o n° de ofertas ativas
    offers = number_offers(soup)
    if not offers:
        return
    if offers > 20:
        return
    print("Offers", offers)

    # lógica para capturar a nota de avaliação do produto
    avaliable = get_avaliable(soup);
    if avaliable and avaliable <= 4:
        return
    print("Avaliable", avaliable);

    # lógica para capturar a marca e realizar seus tratamentos
    brand = get_brand(soup);
    if not brand:
        return
    print("Brand", brand);
