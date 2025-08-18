from config.start_navigator import start
from scripts.collection.insert_in_rabbit import insert_in_rabbit
import time
import random

def list_products(url):
    condition = 'div[role="listitem"]'; # condiciona fixa
    page = 0; # página inicial
    while True:
        page += 1;

        temp_url = url

        if not "&s=exact-aware-popularity-rank" in temp_url:
            temp_url += f"&s=exact-aware-popularity-rank";
        temp_url = temp_url + f"&page={page}";

        soup = start(temp_url, condition);

        cards_product = soup.find_all("div", role="listitem")
        if len(cards_product) > 0:
            for product in cards_product:
                anchor = product.find('a', class_=[
                    'a-link-normal', 
                    's-line-clamp-2', 
                    's-line-clamp-3-for-col-12', 
                    's-link-style', 
                    'a-text-normal'
                ]);
                if not anchor:
                    continue
                href = anchor.get('href');
                link = f"https://amazon.com.br{href}";
                insert_in_rabbit(link);
            time.sleep(random.randint(10, 20));
        else:
            return