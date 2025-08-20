from automation.utils.start_navigator import start
from scripts.product.number_offers import number_offers
from scripts.product.avaliable import get_avaliable
from scripts.product.brand import get_brand
import aio_pika

from automation.inpi.access_inpi import access_inpi

async def scrapping(message: aio_pika.IncomingMessage):
    try:
        url = message.body.decode();

        # processo de inicialização        
        condition = 'div[id="dynamic-aod-ingress-box"]';

        soup = await start(url, condition);

        # print url
        print("Iniciando raspagem...")

        # lógica para capturar o n° de ofertas ativas
        offers = number_offers(soup)
        print(f"[offers] O número retornado da oferta foi '{offers}'")
        if not offers:
            return
        if offers > 20:
            return

        # lógica para capturar a nota de avaliação do produto
        avaliable = get_avaliable(soup);
        print(f"[avaliable] O número retornado da avaliação foi '{avaliable}'")
        if avaliable and avaliable <= 4:
            return

        # passei em alguns filtros, então irei printar o url
        print("\nURL:", url);
        print('\n')

        # lógica para capturar a marca e realizar seus tratamentos
        brand = get_brand(soup);

        brand_database = None
        if brand:
            brand_database = await access_inpi(brand)
        print(f"[brand] A marca retornada foi '{brand_database}'")
        if not brand:
            return
    except:
        return
    