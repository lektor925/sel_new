import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    url = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(url)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(
        (By.ID, 'price'), '$100'))

    button = browser.find_element_by_css_selector('#book')
    button.click()

    x_el = browser.find_element_by_css_selector('#input_value')
    x = x_el.text
    y = calc(x)

    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)

    button = browser.find_element_by_css_selector('#solve')
    button.click()
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
