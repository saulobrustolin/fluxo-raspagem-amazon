from config.start_navigator import start
from scripts.product.number_offers import number_offers
from config.start_navigator import init_browser

def scrapping(ch, method, properties, body):
    url = body.decode();

    # processo de inicialização
    init_browser(headless=True);
    
    condition = 'div[id="dynamic-aod-ingress-box"]';

    soup = start(url, condition);

    # lógica para capturar o n° de ofertas ativas
    offers = number_offers(soup)
    print("Offers", offers)
