def test_items(browser):
    browser.get('http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/')
    button = browser.find_element_by_class_name('btn-add-to-basket')
    assert button, 'button not found!'
