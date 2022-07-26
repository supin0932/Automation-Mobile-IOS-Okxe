from appium import webdriver
import pytest
import unittest
from utils.driversManages import *
from pages.Login_with_username_pwd import *
from pages.Login_with_link import *
from pages.Logout import LogoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.Forget_id_and_pwd import *
from appium.webdriver.common.touch_action import TouchAction

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

    def tearDown(self):
        self.driver.terminate_app('com.okxe')

    def test_forget_pwd_id_with_numberphone_registed_OTPcorrect(self):
        """
        Step 1 : Open app OKXE
        Step 2 : Click button login
        Step 3 : Click button forget password
        Step 4 : Enter numberphone
        Step 5 : Enter opt to sms
        Step 6 : Get username
        Step 7 : Get password
        Step 8 : Enter username and password at login
        Step 9 : Verify account
        *************************
        Data : + Numberphone : Correct
               + OTP : Correct
        Expected Result : Regiter successfull
        """
        pwd = "@Aa246357"
        action = TouchAction(self.driver)
        self.driver.terminate_app('com.okxe')
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.forgetpwdobj.click_button_forget_pwd()
        self.forgetpwdobj.enter_numberphone(numberphone= "0932949905")
        action.tap(x=186, y=152).perform()
        self.forgetpwdobj.click_button_continue()
        self.forgetpwdobj.click_button_autofill_otp()
        self.forgetpwdobj.click_tab_pwd()
        self.forgetpwdobj.enter_pwd(pwd=pwd)
        self.forgetpwdobj.enter_pwd_confirm(pwdcf=pwd)
        action.tap(x=186, y=152).perform()
        self.forgetpwdobj.click_button_update_pwd()
        self.forgetpwdobj.click_button_comback_login()
        self.loginobj.enter_pwd(pwd=pwd)
        self.loginobj.click_button_enter_login()
        self.loginobj.click_logo_account()
        text1 = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        time.sleep(3)
        if text1 == "Lê Minh Nhựt":
            assert True
        else:
            assert False

    def test_forget_pwd_id_with_numberphone_registed_OTPuncorrect(self):
        """
        Step 1 : Open app OKXE
        Step 2 : Click button login
        Step 3 : Click button forget password
        Step 4 : Enter numberphone
        Step 5 : Enter opt any
        Step 6 : Verify page
        *************************
        Data : + Numberphone : Correct
               + OTP : UnCorrect
        Expected Result : Regiter unsuccessfull
        """
        action = TouchAction(self.driver)
        self.driver.terminate_app('com.okxe')
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.forgetpwdobj.click_button_forget_pwd()
        self.forgetpwdobj.enter_numberphone(numberphone="0932949905")
        action.tap(x=186, y=152).perform()
        self.forgetpwdobj.click_button_continue()
        self.forgetpwdobj.enter_otp(n1=1, n2=2, n3=3, n4=4, n5=5, n6=6)
        text = self.loginobj.get_text_warning()
        if text == "Mã xác thực không đúng, vui lòng thử lại.":
            assert True
        else:
            assert False

    def test_forget_pwd_id_with_numberphone_not_registed(self):
        """
        Step 1 : Open app OKXE
        Step 2 : Click button login
        Step 3 : Click button forget password
        Step 4 : Enter numberphone
        Step 5 : Verify page
        *************************
        Data : + Numberphone : Not registed
        Expected Result : Regiter unsuccessfull
        """
        action = TouchAction(self.driver)
        self.driver.terminate_app('com.okxe')
        self.loginobj.click_logo_okxe()
        self.loginobj.click_button_login()
        self.forgetpwdobj.click_button_forget_pwd()
        self.forgetpwdobj.enter_numberphone(numberphone="0932949405")
        action.tap(x=186, y=152).perform()
        self.forgetpwdobj.click_button_continue()
        text = self.loginobj.get_textwarning_numberphone()
        if text == "Số điện thoại này không liên kết với tài khoản nào.":
            assert True
        else:
            assert False


if __name__ == "__main__":
    unittest.main()