import time
import unittest
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from pages.Login_with_link import LoginPage2
from pages.Login_with_username_pwd import *
from pages.Logout import *
from utils.driversManages import *


@pytest.mark.usefixmarkmarktures("driver_Testusefixmarkmarkclass")
class LoginTest1(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities=get_desired_cap1())
        # self.driver = webdriver.Remote(
        #     command_executor='https://nhtl_YNC5cp:ohyhW8iebF6Zsgr3dbiW@hub-cloud.browserstack.com/wd/hub',
        #     desired_capabilities=get_desired_cap())
        self.loginobj = LoginPage1(self.driver)
        self.loginobj1 = LoginPage2(self.driver)
        self.logoutobj = LogoutPage(self.driver)

    def tearDown(self):
        self.driver.terminate_app('vn.okxe.adhoc')

    def test_login_with_usr_pw_is_true(self):
        """
        Username : True
        Password : True
        Expected : Login successfully
        """

        self.driver.terminate_app('vn.okxe.adhoc')
        self.loginobj.click_logo_okxe()
        # try:
        #     time.sleep(3)
        #     self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Don’t Allow").click()
        #     time.sleep(3)
        #     try:
        #         self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Don’t Allow").click()
        #         time.sleep(3)
        #
        #         try:
        #             self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Ask App Not to Track").click()
        #             time.sleep(3)
        #
        #         except:
        #             pass
        #     except:
        #         pass
        # except:
        #     pass
        # try :
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #
        # except :
        #     pass
        self.loginobj.click_button_login()
        self.loginobj.enter_usr(usr="Nhut1176")
        self.loginobj.enter_pwd(pwd="@Nhut1176")
        self.loginobj.click_button_enter_login()
        self.loginobj.click_logo_account()
        text = self.loginobj.get_text_username_account()
        self.logoutobj.click_icon_setting()
        self.logoutobj.click_button_logout()
        self.logoutobj.click_button_confirm_logout()
        time.sleep(3)
        if text == "nhut1176":
            assert True
        else:
            assert False

    def test_login_with_usr_is_true_pw_is_false(self):
        """
        Username : True
        Password : False
        Expected : Login unsuccessfully
        """
        self.driver.terminate_app('vn.okxe.adhoc')
        self.loginobj.click_logo_okxe()
        # try:
        #     time.sleep(3)
        #     self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Don’t Allow").click()
        #     time.sleep(3)
        #     try:
        #         self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Don’t Allow").click()
        #         time.sleep(3)
        #
        #         try:
        #             self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Ask App Not to Track").click()
        #             time.sleep(3)
        #
        #         except:
        #             pass
        #     except:
        #         pass
        # except:
        #     pass
        # try :
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #
        # except :
        #     pass
        self.loginobj.click_button_login()
        self.loginobj.enter_usr(usr="Nhut1176")
        self.loginobj.enter_pwd(pwd="@Aa2463577")
        self.loginobj.click_button_enter_login()
        text = self.loginobj.get_text_warning()
        if text == "Mật khẩu không chính xác, vui lòng kiểm tra lại.":
            assert True
        else:
            assert False

    def test_login_with_usr_is_false_pw_is_true(self):
        """
        Username : False
        Password : True
        Expected : Login unsuccessfully
        """
        self.driver.terminate_app('vn.okxe.adhoc')
        self.loginobj.click_logo_okxe()
        # try:
        #     time.sleep(3)
        #     self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Don’t Allow").click()
        #     time.sleep(3)
        #     try:
        #         self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Don’t Allow").click()
        #         time.sleep(3)
        #
        #         try:
        #             self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Ask App Not to Track").click()
        #             time.sleep(3)
        #
        #         except:
        #             pass
        #     except:
        #         pass
        # except:
        #     pass
        # try :
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #
        # except :
        #     pass
        self.loginobj.click_button_login()
        self.loginobj.enter_usr(usr="Nhut1177")
        self.loginobj.enter_pwd(pwd="@Nhut1176")
        self.loginobj.click_button_enter_login()
        text = self.loginobj.get_text_warning()
        self.driver.terminate_app('com.okxe.app')
        if text == "Tên đăng nhập không tồn tại.":
            assert True
        else:
            assert False

    def test_login_with_usr_pw_is_empty(self):
        """
        Username : Empty
        Password : Empty
        Expected : Login unsuccessfully
        """
        self.driver.terminate_app('vn.okxe.adhoc')
        self.loginobj.click_logo_okxe()
        # try:
        #     time.sleep(3)
        #     self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Don’t Allow").click()
        #     time.sleep(3)
        #     try:
        #         self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Don’t Allow").click()
        #         time.sleep(3)
        #
        #         try:
        #             self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Ask App Not to Track").click()
        #             time.sleep(3)
        #
        #         except:
        #             pass
        #     except:
        #         pass
        # except:
        #     pass
        # try :
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #
        # except :
        #     pass
        self.loginobj.click_button_login()
        self.loginobj.enter_usr(usr="")
        self.loginobj.enter_pwd(pwd="")
        self.loginobj.click_button_enter_login()
        text = self.loginobj.get_text_warning()
        if text == "Thông tin đăng nhập và mật khẩu không được bỏ trống.":
            assert True
        else:
            assert False


    def test_login_with_usr_is_empty(self):
        """
        Username : Empty
        Password : True
        Expected : Login unsuccessfully
        """
        self.driver.terminate_app('vn.okxe.adhoc')
        self.loginobj.click_logo_okxe()
        # try:
        #     time.sleep(3)
        #     self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Don’t Allow").click()
        #     time.sleep(3)
        #     try:
        #         self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Don’t Allow").click()
        #         time.sleep(3)
        #
        #         try:
        #             self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Ask App Not to Track").click()
        #             time.sleep(3)
        #
        #         except:
        #             pass
        #     except:
        #         pass
        # except:
        #     pass
        # try :
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #
        # except :
        #     pass
        self.loginobj.click_button_login()
        self.loginobj.enter_usr(usr="")
        self.loginobj.enter_pwd(pwd="@Nhut1176")
        self.loginobj.click_button_enter_login()
        text = self.loginobj.get_text_warning()
        if text == "Thông tin đăng nhập và mật khẩu không được bỏ trống.":
            assert True
        else:
            assert False


    def test_login_with_pwd_is_empty(self):
        """
        Username : True
        Password : Empty
        Expected : Login unsuccessfully
        """
        self.driver.terminate_app('vn.okxe.adhoc')
        self.loginobj.click_logo_okxe()
        # try:
        #     time.sleep(3)
        #     self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Don’t Allow").click()
        #     time.sleep(3)
        #     try:
        #         self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Don’t Allow").click()
        #         time.sleep(3)
        #
        #         try:
        #             self.driver.find_element(MobileBy.ACCESSIBILITY_ID, "Ask App Not to Track").click()
        #             time.sleep(3)
        #
        #         except:
        #             pass
        #     except:
        #         pass
        # except:
        #     pass
        # try :
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_next_banner()
        #     self.loginobj.click_button_complete_banner()
        #
        # except :
        #     pass
        self.loginobj.click_button_login()
        self.loginobj.enter_usr(usr="Nhut1176")
        self.loginobj.enter_pwd(pwd="")
        self.loginobj.click_button_enter_login()
        text = self.loginobj.get_text_warning()
        if text == "Thông tin đăng nhập và mật khẩu không được bỏ trống.":
            assert True
        else:
            assert False


if __name__ == "__main__":
    unittest.main()
