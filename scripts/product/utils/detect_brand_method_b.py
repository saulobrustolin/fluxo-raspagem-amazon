def detect_brand_method_b(soup):
    try:
        print("[brand] Iniciando a raspagem (método B)...")
        box_general = soup.find('a', id="bylineInfo");
        brand_string = str(box_general.getText());
        brand_lower = brand_string.lower();
        print(f"[brand] Consegui capturar o brand_lower<'{brand_lower}'>, seguindo...")

        param = "visite a loja ";

        search_param = brand_lower.find(param);
        if search_param == -1:
            param = "marca: ";
            search_param = brand_lower.find(param);

        print("[brand] Consegui capturar o tratament_brand, seguindo...")

        brand = brand_lower[len(param):];
        print(f"[brand] Consegui capturar o brand<'{brand}'>, seguindo...")
        
        return str(brand).strip();
    except:
        return