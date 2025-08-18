from playwright.sync_api import sync_playwright
from config.config import headers
from bs4 import BeautifulSoup
import time
import random

_playwright_instance = None
_browser_instance = None

def init_browser(headless=True):
    global _playwright_instance, _browser_instance
    if _playwright_instance is None or _browser_instance is None:
        _playwright_instance = sync_playwright().start()
        _browser_instance = _playwright_instance.chromium.launch(headless=headless, args=["--window-size=1366,768"])
    return _browser_instance

def start(url, condition):
    while True:
        try:
            if _browser_instance is None:
                raise Exception("Navegador não inicializado! Chame init_browser() antes.")

            page = _browser_instance.new_page(
                extra_http_headers=headers,
                viewport={
                    "width": 1366,
                    "height": 768
                })
            
            page.goto(url)
            page.wait_for_selector(condition, timeout=10000)
            html = page.content()
            page.close()
            return BeautifulSoup(html, "html.parser")
        
         # se der erro no carregamento da página
        except:
            page.close();
            time.sleep(random.randint(20, 40));
            continue

def close():
    global _playwright_instance, _browser_instance
    if _browser_instance:
        _browser_instance.close()
        _browser_instance = None
    if _playwright_instance:
        _playwright_instance.stop()
        _playwright_instance = None
    print('\nBrowser finalizado com sucesso!')
