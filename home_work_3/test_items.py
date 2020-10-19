from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# Добавлена проверка на видимость кнопки
# При необходимости добавлена проверка на кликабельность кнопки


def test_button_to_cart_should_on_page(browser):
    browser.get(link)
    time.sleep(30)
    button_vis = WebDriverWait(browser, 10).until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket")))
    assert button_vis, "кнопка не находится в DOM И невидима или имеет ширину и высоту равную 0"


# def test_button_to_cart_should_clickable(browser):
#     browser.get(link)
#     time.sleep(30)
#     button_click = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".btn-add-to-basket")))
#     assert button_click, "кнопка не кликабельна"