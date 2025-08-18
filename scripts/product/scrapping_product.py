from config.start_navigator import start
from scripts.product.number_offers import number_offers
from scripts.product.avaliable import avaliable
from config.start_navigator import init_browser

def scrapping(ch, method, properties, body):
    url = body.decode();

    # processo de inicialização
    init_browser(headless=True);
    
    condition = 'div[id="dynamic-aod-ingress-box"]';

    soup = start(url, condition);

    # lógica para capturar o n° de ofertas ativas
    offers = number_offers(soup)
    if not offers:
        return
    if offers > 20:
        return
    print("Offers", offers)

    # lógica para capturar a nota de avaliação do produto
    avaliable = avaliable(soup)
    if avaliable and avaliable <= 4:
        return
    print("Avaliable", avaliable)

    # lógica para capturar a marca e realizar seus tratamentos
