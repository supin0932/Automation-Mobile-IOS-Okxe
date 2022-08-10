from locators.logoutLocator import *
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from appium.webdriver.common.touch_action import TouchAction

class LoginGmail:
    def __init__(self, driver):
        self.driver = driver

    def login_account_gm(self, username, pwd):
        action = TouchAction(self.driver)
        print("Login account gmail.com")
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, 'Safari')))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.XPATH, "//XCUIElementTypeOther[@name='CapsuleViewController']/XCUIElementTypeOther[3]")))
        CLICK.clear()
        CLICK.send_keys("gmail.com")
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Go")))
        CLICK.click()
        time.sleep(10)
        action.tap(x=159, y=252).perform()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Email hoặc số điện thoại")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Email hoặc số điện thoại")))
        CLICK.send_keys(username)
        time.sleep(1)
        action.tap(x=290, y=369).perform()
        time.sleep(3)
        action.tap(x=289, y=392).perform()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Nhập mật khẩu của bạn")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Nhập mật khẩu của bạn")))
        CLICK.send_keys(pwd)
        time.sleep(1)
        action.tap(x=290, y=369).perform()
        time.sleep(3)
        action.tap(x=289, y=392).perform()
        time.sleep(5)
        self.driver.terminate_app('com.apple.mobilesafari')

    def enter_user_pwd_gmail(self, username, pwd):
        print("Enter account gmail")
        action = TouchAction(self.driver)
        time.sleep(5)
        action.tap(x=176, y=348).perform()
        time.sleep(1)
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Email hoặc số điện thoại")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Email hoặc số điện thoại")))
        CLICK.send_keys("lenhut20121995@gmail.com")
        time.sleep(1)
        action.tap(x=290, y=369).perform()
        time.sleep(3)
        action.tap(x=289, y=392).perform()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Nhập mật khẩu của bạn")))
        CLICK.click()
        CLICK = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Nhập mật khẩu của bạn")))
        CLICK.send_keys("11762115")
        time.sleep(1)
        action.tap(x=290, y=369).perform()
        time.sleep(3)
        action.tap(x=290, y=425).perform()

    def click_select_account_gmail(self):
        print("Select account")
        time.sleep(5)
        CLICK = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID,"nhựt lê lenhut20121995@gmail.com")))
        CLICK.click()
