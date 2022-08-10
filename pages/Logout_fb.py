from locators.logoutLocator import *
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.multi_action import *
import time
from appium.webdriver.common.touch_action import TouchAction

class LogoutFacebook:
    def __init__(self, driver):
        self.driver = driver

    def logout_facebook(self):
        print("Logout Facebook")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, 'Safari')))
        CLICK.click()
        time.sleep(3)
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, 'Menu chính')))
        CLICK.click()
        time.sleep(3)
        self.driver.swipe(300, 500, 100, 300, 1000)
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, '(//XCUIElementTypeLink[@name="Đăng xuất"])[1]')))
        CLICK.click()
        click_login = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Thay đổi thông tin Lê Nhựt đã lưu trên thiết bị này")))
        click_login.click()
        click_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH,
                                                                                       "//XCUIElementTypeButton[@name='Gỡ tài khoản khỏi thiết bị']")))
        click_login.click()
        time.sleep(2)
        self.driver.terminate_app('com.apple.mobilesafari')
