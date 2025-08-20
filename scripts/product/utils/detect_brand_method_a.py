def detect_brand_method_a(soup):
    try:
        print("[brand] Iniciando a raspagem (método A)...")
        box_general = soup.find('p', id="pqv-byline");
        brand_string = str(box_general.getText());
        brand_lower = brand_string.lower();

        param = "de ";

        tratament_brand = brand_lower.find(param);

        brand = tratament_brand[len(param):];
        
        return str(brand).strip();
    except:
        return