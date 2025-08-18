def avaliable(soup):
    try:
        box_general = soup.find('span', id='acrCustomerReviewText');
        return str(box_general.getText()).strip();
    except:
        return