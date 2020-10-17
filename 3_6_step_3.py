import time
import math
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize("step", ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
# @pytest.mark.parametrize("step", ["236895", "236896"])
def test_my_work(browser, step):
    link = f"https://stepik.org/lesson/{step}/step/1"
    browser.get(link)

    # my_textarea = browser.find_element_by_css_selector("textarea[data-autogrow]")
    ta_css = 'textarea[data-autogrow]'
    my_textarea = WebDriverWait(browser, 25).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ta_css))
    )
    # answer = int(math.log(int(time.time())))
    answer = str(math.log(int(time.time()-2)))
    # print(answer)
    my_textarea.send_keys(answer)
    button = WebDriverWait(browser, 25).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    button.click()

    msg_el = WebDriverWait(browser, 25).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    msg_text = msg_el.text
    print(msg_text)
    assert msg_text == 'Correct!', 'Неверный ответ'
