def get_avaliable(soup):
    try:
        box_general = soup.find('span', id='acrPopover');
        tratament_avaliable = str(box_general.get('title')).strip();
        print(tratament_avaliable)

        capture_avaliable = tratament_avaliable[0:3];
        replace_avaliable = capture_avaliable.replace(',', '.');

        return int(replace_avaliable)
    except:
        return