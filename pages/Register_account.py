from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.registerLocator import *
from appium import webdriver
import time
class RegisterAccount:
    def __init__(self, driver):
        self.driver = driver

    def click_register_button(self):
        print("Click register button")
        click_button_register = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_button_register_accessid())))
        click_button_register.click()


    def enter_username_register(self, username):
        print("Enter username register")
        enter_user = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "oka_sign_up_screen_username_input_view")))
        enter_user.clear()
        enter_user.send_keys(username)

    def enter_password_register(self, pwd):
        print("Enter password register")
        enter_pwd = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_enter_pwd_accessid())))
        enter_pwd.clear()
        enter_pwd.send_keys(pwd)

    def enter_password_confirm_register(self, pwdcf):
        print("Enter password confirm")
        enter_pwd = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_enter_pwd_confirm_accessid())))
        enter_pwd.clear()
        enter_pwd.send_keys(pwdcf)

    def click_enter_register_button(self):
        print("Click enter register button")
        click_button_register = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_button_enter_register_accessid())))
        click_button_register.click()

    def click_button_comeback_home(self):
        print("Click button comback home")
        click_button_comeback_home = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "oka_success_screen_return_to_home_button")))
        click_button_comeback_home.click()

    def click_button_update_profile(self):
        print("Click button update profile")
        click_button_update_profile = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "oka_success_screen_update_profile_button")))
        click_button_update_profile.click()


