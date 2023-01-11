import pytest

from Config.config import config
from Page.BaseKeywords import BaseKeywords


class HomePage(BaseKeywords):

    inputid = "#id=fullName"
    editbtn= "#text=Edit"

    def __init__(self, driver):
        super().__init__(driver)

    def get_Title(self):
        return self.getTitle()

    def click_input(self):
        self.click_OnText(self.editbtn)

    def fill_Name(self):
        value = self.send_keys(self.inputid, "Chidambaram")
        print(value)

    def homePage_Check(self):
        self.getTitle()
        self.click_On(self.editbtn)
        value = self.send_keys(self.inputid, "Chidambaram")
        print(value)