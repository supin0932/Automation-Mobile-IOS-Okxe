from locators.forgetpasswordLocator import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.loginLocator import *
from appium.webdriver.common.mobileby import MobileBy

class ForgetPassword:
    def __init__(self, driver):
        self.driver = driver

    def click_button_forget_pwd(self):
        print("Click forget password")
        click_button_fg_pwd = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_button_forget_pwd_accessid())))
        click_button_fg_pwd.click()

    def enter_numberphone(self, numberphone):
        print("Enter numberphone")
        enter_numberphone = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_enter_numberphone_acessid())))
        enter_numberphone.send_keys(numberphone)

    def enter_otp(self, n1, n2, n3, n4, n5, n6):
        print("Enter opt")
        enter_n1 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_nb1_otp_accessid())))
        enter_n1.send_keys(n1)
        enter_n2 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_nb2_otp_accessid())))
        enter_n2.send_keys(n2)
        enter_n3 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_nb3_otp_accessid())))
        enter_n3.send_keys(n3)
        enter_n4 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_nb4_otp_accessid())))
        enter_n4.send_keys(n4)
        enter_n5 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_nb5_otp_accessid())))
        enter_n5.send_keys(n5)
        enter_n6 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_nb6_otp_accessid())))
        enter_n6.send_keys(n6)

    def click_button_continue(self):
        print("Click button continue")
        click_button_continue = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_button_continue_accessid())))
        click_button_continue.click()


    def click_tab_username(self):
        print("Click tab username")
        click_tab_usr = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_tab_usrname_accessid())))
        click_tab_usr.click()

    def get_username(self):
        print("Get username")
        get_usr = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, "//XCUIElementTypeTextField[@name='rounded_text_field']"))).text
        return get_usr

    def click_tab_pwd(self):
        print("Click tab password")
        click_tab_pwd = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_tab_pwd_accessid())))
        click_tab_pwd.click()

    def enter_pwd(self, pwd):
        print("Enter password")
        enter_pwd = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_enter_new_pwd_accessid())))
        enter_pwd.send_keys(pwd)

    def enter_pwd_confirm(self, pwdcf):
        print("Enter password confirm")
        enter_pwd_confirm = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_enter_new_pwd_confirm_accessid())))
        enter_pwd_confirm.send_keys(pwdcf)

    def click_button_comback_login(self):
        print("Click button comback login")
        click_bt_cb_lg = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.XPATH, "//XCUIElementTypeButton[@name='Về trang đăng nhập']")))
        click_bt_cb_lg.click()

    def click_button_update_pwd(self):
        print("Click button update password")
        click_bt_up_pwd = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ID, get_button_update_pwd_accessid())))
        click_bt_up_pwd.click()

    def click_button_autofill_otp(self):
        print("Click button autofill otp")
        click_bt_up_pwd = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, get_button_autofill_otp_acessid())))
        click_bt_up_pwd.click()