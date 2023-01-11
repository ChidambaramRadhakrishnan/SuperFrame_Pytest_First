from Page.button_click import click_Btn
from Test.Test_base import baseTest


class Test_ButtonClickPage(baseTest):

    def test_clickButton(self):
        self.button = click_Btn(self.driver)
        self.button.get_Title()
        self.button.click_btn()
        self.button.click_goto_Home()
