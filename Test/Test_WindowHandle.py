from Page.homePage import HomePage
from Page.window_Handle import windowHandle
from Test.Test_base import baseTest
import time
from Config.log import log
import pytest


class Test_Window_Handles(baseTest):

    logs = log.logs()

    @pytest.mark.smoke
    def test_Window_Handles(self):
        self.logs.info("*******************Test has been Initiated***************")
        self.window = windowHandle(self.driver)
        self.window.click_Tabs()
        self.logs.info("*********The window page has loaded*********")
        get_window: object = self.window.get_window()
        self.window.click_Multiple_Window()
        self.window.click_Multiple_Window()
        self.logs.info("*********The window page has loaded*********")
        self.window.switch_to_main_window(get_window)
        self.window.switch_to_specific_window()
        self.logs.info("*********The window has Switched*********")
        time.sleep(1)

    @pytest.mark.smoke
    def test_sendKeys(self):
        self.home = HomePage(self.driver)
        self.home.homePage_Check()
        time.sleep(2)


