import time


def test_language(browser):
    link = f"http://selenium1py.pythonanywhere.com/{browser[1]}/catalogue/coders-at-work_207/"
    browser[0].get(link)
    time.sleep(10)
    browser[0].find_element_by_css_selector("#add_to_basket_form > button")
