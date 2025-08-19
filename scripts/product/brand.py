def get_brand(soup):
    try:
        box_general = soup.find('p', id="pqv-byline");
        print("box_general:", box_general);
        brand_string = str(box_general.getText());
        print("brand_string:", brand_string);
        brand_string = brand_string.lower();

        param = "brand de ";

        tratament_brand = brand_string.find(param);

        brand = tratament_brand[len(param):];
    
        return str(brand).strip();
    except:
        return