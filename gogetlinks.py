import math
import time

from selenium import webdriver


try:
    # авторизация на сайте
    url = 'https://gogetlinks.net/'
    login = 'partizan925@mail.ru'
    passw = 'Djpyzr925'
    browser = webdriver.Chrome()
    browser.get(url)

    login_input = browser.find_element_by_css_selector('#login_e_mail')
    login_input.send_keys(login)

    passw_input = browser.find_element_by_css_selector('#login_password')
    passw_input.send_keys(passw)

    button = browser.find_element_by_css_selector('#ok_button')
    button.click()

    time.sleep(2)

    link = browser.find_element_by_css_selector('a[href="/search_sites.php"]')
    link.click()

    # поиск ссылок
    time.sleep(4)
    current_page = browser.find_elements_by_css_selector('.links_pages_current + a')[1]
    browser.execute_script("return arguments[0].scrollIntoView(true);", current_page)
    current_page.click()
    # поиск ссылок
    time.sleep(4)
    current_page = browser.find_elements_by_css_selector('.links_pages_current + a')[1]
    browser.execute_script("return arguments[0].scrollIntoView(true);", current_page)
    current_page.click()
    # поиск ссылок
    time.sleep(4)
    current_page = browser.find_elements_by_css_selector('.links_pages_current + a')[1]
    browser.execute_script("return arguments[0].scrollIntoView(true);", current_page)
    current_page.click()
    # поиск ссылок
    time.sleep(4)
    current_page = browser.find_elements_by_css_selector('.links_pages_current + a')[1]
    browser.execute_script("return arguments[0].scrollIntoView(true);", current_page)
    current_page.click()


finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()
