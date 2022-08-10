from appium import webdriver
import time
import pytest
import unittest
from appium.webdriver.common.touch_action import TouchAction
from pages.Forget_id_and_pwd import ForgetPassword
from pages.Register_account import RegisterAccount
from utils.driversManages import *
from pages.Login_with_username_pwd import *
from pages.Login_with_link import *
from pages.Logout import LogoutPage
from appium.webdriver.common.multi_action import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixmarkmarktures("driver_Testusefixmarkmarkclass")
class LoginTest2(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities=get_desired_cap1())
        # self.driver = webdriver.Remote(
        #     command_executor='https://lminhnht_Z0PVgW:YBp4r6LvTMj95us59PuD@hub-cloud.browserstack.com/wd/hub',
        #     desired_capabilities=get_desired_cap())
        self.loginobj = LoginPage1(self.driver)
        self.loginobj1 = LoginPage2(self.driver)
        self.logoutobj = LogoutPage(self.driver)
        self.forgetpwdobj = ForgetPassword(self.driver)
        self.registerobj = RegisterAccount(self.driver)

    def tearDown(self):
        ""
        # self.driver.terminate_app('com.okxe')

    def test_register_with_numberphone_correct_not_register(self):
        username = "test1176"
        pwd = "@Aa246357"
        action = TouchAction(self.driver)
        self.driver.terminate_app('com.okxe')
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.registerobj.click_register_button()
        self.forgetpwdobj.enter_numberphone(numberphone="0932241574")
        action.tap(x=186, y=152).perform()
        self.forgetpwdobj.click_button_continue()
        self.registerobj.enter_username_register(username=username)
        self.registerobj.enter_password_register(pwd=pwd)
        self.registerobj.enter_password_confirm_register(pwdcf=pwd)
        action.tap(x=186, y=152).perform()
        self.registerobj.click_enter_register_button()
        self.forgetpwdobj.click_button_autofill_otp()
        self.registerobj.click_button_comeback_home()
        self.loginobj.click_logo_account()
        text1 = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        time.sleep(3)
        if text1 == username:
            assert True
        else:
            assert False

    def test_register_with_numberphone_correct_registed(self):
        username = "test1176"
        pwd = "@Aa246357"
        action = TouchAction(self.driver)
        self.driver.terminate_app('com.okxe')
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.registerobj.click_register_button()
        self.forgetpwdobj.enter_numberphone(numberphone="")
        action.tap(x=186, y=152).perform()
        self.forgetpwdobj.click_button_continue()



if __name__ == "__main__":
    unittest.main()