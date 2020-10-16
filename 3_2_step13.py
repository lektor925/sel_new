import unittest

from selenium import webdriver
import time


class PageTest(unittest.TestCase):
    def test_first_page(self):
        link = "http://suninjuly.github.io/registration1.html"

        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(1)

        # Ваш код, который заполняет обязательные поля
        name = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
        name.send_keys('Ivan')

        surname = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
        surname.send_keys('Ivanov')

        mail = browser.find_element_by_css_selector("input[placeholder='Input your email']")
        mail.send_keys('ivanov@test.ru')
        time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_second_page(self):
        link = "http://suninjuly.github.io/registration2.html"

        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(1)

        # Ваш код, который заполняет обязательные поля
        name = browser.find_element_by_css_selector("input[placeholder='Input your first name']")
        name.send_keys('Ivan')

        surname = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
        surname.send_keys('Ivanov')

        mail = browser.find_element_by_css_selector("input[placeholder='Input your email']")
        mail.send_keys('ivanov@test.ru')
        time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()
