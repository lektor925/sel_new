import math
import time

from selenium import webdriver


try:
    url = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(url)

    num1_el = browser.find_element_by_css_selector('#num1')
    num1 = int(num1_el.text)

    num2_el = browser.find_element_by_css_selector('#num2')
    num2 = int(num2_el.text)

    sum = num1 + num2
    opt = f'[value="{str(sum)}"]'

    select = browser.find_element_by_css_selector('#dropdown').click()
    options = browser.find_element_by_css_selector(opt).click()

    button = browser.find_element_by_css_selector('button')
    button.click()
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
