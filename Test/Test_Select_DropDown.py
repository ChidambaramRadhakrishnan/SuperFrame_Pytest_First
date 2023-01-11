import time

from Page.DropDownpage import dropdown_Page
from Test.Test_base import baseTest
from Config.log import log


class Test_dropdown(baseTest):
    logs = log.logs()

    def test_select_dropdown(self):
        self.logs.info("-------------Select Drop Down Page ******************")
        self.select = dropdown_Page(self.driver)
        self.logs.info("***************** Driver has launched *****************")
        self.select.get_Title()
        p = self.select.click_Select_Button()
        self.logs.info("***************** Page Title is ******************")
        # self.select.click_dropdown()
        self.select.select_dropdowns()
        self.logs.info("***************** Select Drop Downs ******************")
        time.sleep(5)
