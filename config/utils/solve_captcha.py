from bs4 import BeautifulSoup
import time

def solve_captcha(page):
    try:
        condition = "form[action='/errors/validateCaptcha']";

        page.wait_for_selector(condition, timeout=10000);

        # clica no botão dentro do form
        page.click("form[action='/errors/validateCaptcha'] button[alt='Continuar comprando']");

        # espera 1 segundo para renderizar a pagina
        time.sleep(1)

        html = page.content();

        page.close();

        return BeautifulSoup(html, "html.parser");
    except:
        return