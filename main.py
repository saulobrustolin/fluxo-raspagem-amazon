from scripts.collection.list_products import list_products
from config.start_navigator import init_browser, close

def main():
    url = "https://www.amazon.com.br/s?me=AWB62XDVP19UK&marketplaceID=A2Q3Y263D00KWC&s=exact-aware-popularity-rank";

    # processo de inicialização
    init_browser();

    # lógica para pegar os itens  
    list_products(url);

    close();

main();
