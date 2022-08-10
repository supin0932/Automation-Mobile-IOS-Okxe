from locators.logoutLocator import *
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.common.touch_action import TouchAction

class LoginFacebook:
    def __init__(self, driver):
        self.driver = driver


    def login_account_fb(self, username, pwd):
        print("Login account facebook")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, 'Safari')))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, "//XCUIElementTypeOther[@name='CapsuleViewController']/XCUIElementTypeOther[3]")))
        CLICK.clear()
        CLICK.send_keys("facebook.com")
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Go")))
        CLICK.click()

        # try:
        #     CLICK = WebDriverWait(self.driver, 5).until(
        #         EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, 'Safari')))
        #     CLICK.click()
        # except:
        #     pass
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, "//XCUIElementTypeOther[@name='main']/XCUIElementTypeTextField")))
        CLICK.send_keys(username)
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, "//XCUIElementTypeOther[@name='main']/XCUIElementTypeSecureTextField")))
        CLICK.send_keys(pwd)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, "//XCUIElementTypeButton[@name='Đăng nhập']")))
        CLICK.click()
        try:
            CLICK = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Lúc khác")))
            CLICK.click()
            time.sleep(5)
        except:
            pass
        self.driver.terminate_app('com.apple.mobilesafari')

    def enter_user_pwd_facebook(self, username, pwd):
        print("Enter account facebook")
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, "//XCUIElementTypeOther[@name='main']/XCUIElementTypeTextField")))
        CLICK.clear()
        CLICK.send_keys(username)
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, "//XCUIElementTypeOther[@name='main']/XCUIElementTypeSecureTextField")))
        CLICK.send_keys(pwd)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, "//XCUIElementTypeButton[@name='Đăng nhập']")))
        CLICK.click()
        try:
            CLICK = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Tiếp tục")))
            CLICK.click()
        except:
            pass