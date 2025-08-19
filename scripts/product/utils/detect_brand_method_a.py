def detect_brand_method_a(soup):
    try:
        print("[brand] Iniciando a raspagem (método A)...")
        box_general = soup.find('p', id="pqv-byline");
        brand_string = str(box_general.getText());
        print("[brand] brand_string:", brand_string);
        brand_lower = brand_string.lower();
        print(f"[brand] Consegui capturar o brand_lower<'{brand_lower}'>, seguindo...")

        param = "de ";

        tratament_brand = brand_lower.find(param);
        print("[brand] Consegui capturar o tratament_brand, seguindo...")

        brand = tratament_brand[len(param):];
        print("[brand] Consegui capturar o brand, seguindo...")
        
        return str(brand).strip();
    except:
        return