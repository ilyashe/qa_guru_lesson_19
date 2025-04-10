from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search(ios_management):
    with step('Click button'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
    with step('Type email'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).send_keys("hello@browserstack.com" + "\n")
    with step('Check email'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(have.text('hello@browserstack.com'))
