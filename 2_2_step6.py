import math
import time

from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    url = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(url)

    x_el = browser.find_element_by_css_selector('#input_value')
    x = int(x_el.text)
    y = calc(x)

    input = browser.find_element_by_css_selector('#answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)
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
