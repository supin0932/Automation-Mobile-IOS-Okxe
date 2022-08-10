from locators.logoutLocator import *
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.multi_action import *
import time
from appium.webdriver.common.touch_action import TouchAction

class LogoutGmail:
    def __init__(self, driver):
        self.driver = driver

    def logout_gmail(self):
        """Đăng xuất gmail"""
        print("Logout Gmail")
        action = TouchAction(self.driver)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, 'Safari')))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Menu")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, "//XCUIElementTypeButton[@name='lenhut20121995@gmail.com']")))
        CLICK.click()
        time.sleep(2)
        action.tap(x=179, y=256).perform()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,"//XCUIElementTypeOther[@name='Gmail']/XCUIElementTypeOther[3]/XCUIElementTypeOther[4]")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,"//XCUIElementTypeLink[@name='nhựt lê lenhut20121995@gmail.com']")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Có, hãy xóa")))
        CLICK.click()
        time.sleep(5)
        self.driver.terminate_app('com.apple.mobilesafari')