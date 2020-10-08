import os
import time

from selenium import webdriver


try:
    url = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(url)

    name = browser.find_element_by_css_selector('[name="firstname"]')
    name.send_keys('Ivan')

    surname = browser.find_element_by_css_selector('[name="lastname"]')
    surname.send_keys('Ivanov')

    email = browser.find_element_by_css_selector('[name="email"]')
    email.send_keys('ivanov@test.ru')

    file_input = browser.find_element_by_css_selector('[name="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    file_input.send_keys(file_path)

    button = browser.find_element_by_css_selector('button')
    button.click()
finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
