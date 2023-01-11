import pytest
import time

from Page.homePage import HomePage
from Test.Test_base import baseTest
from Config.config import  config


class TestHome(baseTest):

    def test_input(self):
        self.home = HomePage(self.driver)
        title = self.home.get_Title()
        assert title == config.PageTitle
        self.home.click_input()
        self.home.fill_Name()
        time.sleep(10)
