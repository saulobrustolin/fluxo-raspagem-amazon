def get_avaliable(soup):
    try:
        box_general = soup.find('span', id='acrPopover');
        tratament_avaliable = str(box_general.get('title')).strip();

        capture_avaliable = tratament_avaliable[0:3];
        replace_avaliable = capture_avaliable.replace(',', '.');

        return float(replace_avaliable)
    except:
        return