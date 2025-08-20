from bs4 import BeautifulSoup
import asyncio

async def solve_captcha(page):
    try:
        condition = "form[action='/errors/validateCaptcha']";

        await page.wait_for_selector(condition, timeout=10000);

        # clica no botão dentro do form
        await page.click("form[action='/errors/validateCaptcha'] button[alt='Continuar comprando']");

        # espera 1 segundo para renderizar a pagina
        await asyncio.sleep(2)

        html = await page.content();

        await page.close();

        return BeautifulSoup(html, "html.parser");
    except:
        return