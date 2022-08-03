from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.loginLocator import *
from appium import webdriver
import time
class RegisterAccount:
    def __init__(self, driver):
        self.driver = driver

    def click_register_button(self):
        print("Click register button")
        click_button_next_banner = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID,get_button_next_banner_id())))
        click_button_next_banner.click()

    def click_username_register(self):
        print("Click username register")
        click_usr_rg = self.driver.find_element_by_xpath(get_usr_register_xpath())
        click_usr_rg.click()

    def enter_username_register(self, username):
        print("Enter username register")
        enter_usr_rg = self.driver.find_element_by_xpath(get_usr_register_xpath())
        enter_usr_rg.clear()
        enter_usr_rg.send_keys(username)

    def click_pwd_register(self):
        print("Click password register")
        click_pwd_rg = self.driver.find_element_by_xpath(get_pwd_register_xpath())
        click_pwd_rg.click()

    def enter_pwd_register(self, pwd):
        print("Enter password register")
        enter_pwd_rg = self.driver.find_element_by_xpath(get_pwd_register_xpath())
        enter_pwd_rg.clear()
        enter_pwd_rg.send_keys(pwd)

    def click_pwd_register_confirm(self):
        print("Click password register confirm")
        click_pwd_rg_cf = self.driver.find_element_by_css_selector(get_pwd_register_confirm_css())
        click_pwd_rg_cf.click()

    def enter_pwd_register_confirm(self, pwd):
        print("Enter password register confirm")
        enter_pwd_rg = self.driver.find_element_by_css_selector(get_pwd_register_confirm_css())
        enter_pwd_rg.clear()
        enter_pwd_rg.send_keys(pwd)

    def click_register(self):
        print("Click register")
        click_rg = self.driver.find_element_by_xpath(get_register_button_xpath())
        click_rg.click()

