import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.browser import set_driver, quit_driver


def pytest_addoption(parser):
    """
    для запуска :
        pytest -s -v --tb=short --browser_name=firefox test_conftest.py
        pytest -s -v --tb=short --browser_name=chrome --language=en test_conftest.py
        pytest -s -v --tb=line test_main_page.py
    """
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language browser: ru,en,es... (default - en)")


@pytest.fixture(scope="function")
def set_browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print(f"\nuser language: {user_language}\nstart {browser_name} browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        set_driver(webdriver.Chrome(options=options))
    elif browser_name == "firefox":
        print(f"\nuser language: {user_language}\nstart {browser_name} browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        set_driver(webdriver.Firefox(firefox_profile=fp))
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield
    print("\nquit browser..")
    quit_driver()
