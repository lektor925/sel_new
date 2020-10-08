import math
import time

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    url = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(url)

    button = browser.find_element_by_css_selector('button')
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x_el = browser.find_element_by_css_selector('#input_value')
    x = x_el.text
    y = calc(x)

    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)

    button = browser.find_element_by_css_selector('button')
    button.click()
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
