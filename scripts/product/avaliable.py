def get_avaliable(soup):
    try:
        print("[available] Iniciando a raspagem...")
        box_general = soup.find('span', id='acrPopover');
        print("[avaliable] Consegui capturar o box_general, seguindo...")
        tratament_avaliable = str(box_general.get('title')).strip();
        print("[avaliable] Consegui capturar o tratament_avaliable, seguindo...")

        capture_avaliable = tratament_avaliable[0:3];
        print("[avaliable] Consegui capturar o capture_avaliable, seguindo...")
        replace_avaliable = capture_avaliable.replace(',', '.');
        print("[avaliable] Consegui fazer o replace_avaliable, seguindo...")

        return float(replace_avaliable)
    except:
        return