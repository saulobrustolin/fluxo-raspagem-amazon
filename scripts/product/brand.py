from scripts.product.utils.detect_brand_method_a import detect_brand_method_a
from scripts.product.utils.detect_brand_method_b import detect_brand_method_b

def get_brand(soup):
    brand = detect_brand_method_a(soup);
    if brand and brand != "None":
        return brand
    brand = detect_brand_method_b(soup);
    if brand and brand != "None":
        return brand
    print('[brand] Não foi possível capturar a marca, abortando...')