from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()  # Chrome driver
        print("Launching Chrome Browser")
    elif browser == 'ie':
        driver = webdriver.Ie()  # Internet Explorer driver
        print("Launching Internet Explorer Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()  # Firefox driver
        print("Launching Firefox Browser")
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(10)  # Optional: Implicit wait for elements to load
    yield driver

    driver.quit()


def pytest_addoption(parser):
    print(parser)
    parser.addoption("--browser",action="store", default="chrome", help="Specify browser: chrome, firefox or ie")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
