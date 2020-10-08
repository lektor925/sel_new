import time
from selenium import webdriver

# url = "http://suninjuly.github.io/registration1.html"
url2 = "http://suninjuly.github.io/registration2.html"

with webdriver.Chrome() as browser:
    browser.get(url2)
    try:
        required = {
            'first_name':browser.find_element_by_xpath('//label[text() = "First name*"]/following::input'),
            'last_name':browser.find_element_by_xpath('//label[text() = "Last name*"]/following::input'),
            'email':browser.find_element_by_xpath('//label[text() = "Email*"]/following::input'),
        }
    except:
        raise Exception('Сheck the required fields!')
    for el in required:
        required[el].send_keys('test')
    browser.find_element_by_class_name('btn').click()
    time.sleep(1)
    text = browser.find_element_by_tag_name('h1').text
    assert text == "Congratulations! You have successfully registered!"