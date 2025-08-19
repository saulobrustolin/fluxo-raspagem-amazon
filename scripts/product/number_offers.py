from scripts.product.utils.detect_span import detect_span

def number_offers(soup):
    try:
        print("[offers] Iniciando a raspagem...")
        span_list = soup.find_all('span', class_='a-color-base');
        print("[offers] Consegui pegar a lista de span, seguindo...\n")

        # detectar qual é o span que possui
        span_brute = detect_span(span_list);
        print(f"[offers] Consegui detectar o span correto<'{span_brute}'>, seguindo...")
        if not span_brute:
            return 1
        if span_brute:
            return int(span_brute.strip())
    except:
        return