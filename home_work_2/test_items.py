import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."

def test_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    assert len(browser.find_elements_by_css_selector(".btn-add-to-basket"))==1, "the button add-to-basket isn't present on the page or selector already isn't unique"