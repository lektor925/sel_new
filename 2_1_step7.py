import math
import time

from selenium import webdriver


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    url = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(url)

    x_element = browser.find_element_by_css_selector('#treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input = browser.find_element_by_css_selector('#answer')
    input.send_keys(y)

    chekbox = browser.find_element_by_css_selector('#robotCheckbox')
    chekbox.click()

    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()

    button = browser.find_element_by_css_selector('button')
    button.click()
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
