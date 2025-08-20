def detect_brand_method_b(soup):
    try:
        print("[brand] Iniciando a raspagem (método B)...")
        box_general = soup.find('a', id="bylineInfo");
        brand_string = str(box_general.getText());
        brand_lower = brand_string.lower();

        param = "visite a loja ";

        search_param = brand_lower.find(param);
        if search_param == -1:
            param = "marca: ";
            search_param = brand_lower.find(param);


        brand = brand_lower[len(param):];
        
        return str(brand).strip();
    except:
        return