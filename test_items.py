import time


def test_items(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = browser.find_element_by_class_name('btn-add-to-basket')
    #time.sleep(100)
    assert button, 'button not found!'
