import time
import math
import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


# @pytest.mark.parametrize("step", ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
@pytest.mark.parametrize("step", ["236895", "236896"])
def test_my_work(browser, step):
    link = f"https://stepik.org/lesson/{step}/step/1"
    browser.get(link)
    browser.implicitly_wait(75)

    my_textarea = browser.find_element_by_css_selector("textarea")
    answer = math.log(int(time.time()))
    my_textarea.send_keys(answer)
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()

    msg_text = browser.find_element_by_css_selector(".smart-hints__hint").text
    print(msg_text)
    assert msg_text == 'Correct!', 'Неверный ответ'
