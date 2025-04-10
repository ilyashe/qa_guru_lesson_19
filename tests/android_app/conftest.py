import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser, support
import os

from config import config
from selene_in_action import utils

from appium import webdriver


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        # 'platformName': 'android',
        'platformVersion': '9.0',
        'deviceName': 'Google Pixel 3',

        # Set URL of the application under test
        'app': 'bs://02ab46887d0bba94114568768536f93a6de07d68',
        "appWaitActivity": "org.wikipedia.*",

        # Set other BrowserStack capabilities
        'bstack:options': {
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            # Set your access credentials
            'userName': config.bstack_userName,
            'accessKey': config.bstack_accessKey,
        }
    })

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub',
            options=options
        )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    utils.attach.attach_screenshot(browser)
    utils.attach.attach_xml(browser)


    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    utils.attach.attach_bstack_video(session_id)
