import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: es supported only")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    if language == 'es':
        browser = webdriver.Chrome(options=options)
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    else:
        print("I dont know this language".format(language))
    yield browser
    print("\nquit browser..")
    browser.quit()
