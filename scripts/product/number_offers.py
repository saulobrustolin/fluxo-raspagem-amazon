from scripts.product.utils.detect_span import detect_span
from scripts.product.utils.tratament_span_offers import tratament_span_offers

def number_offers(soup):
    box_general = soup.find('div', id='dynamic-aod-ingress-box');
    span_list = box_general.find_all('span', class_='a-color-base');

    # detectar qual é o span que possui
    span_brute = detect_span(span_list);
    if not span_brute:
        return 1

    span_clean = tratament_span_offers(span_brute.getText());
    span_clean = str(span_clean).strip()
    if span_clean:
        return int(span_clean)