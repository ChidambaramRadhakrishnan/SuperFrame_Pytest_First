from Page.TablePage import TestPage
from Test.Test_base import baseTest
import time


class Test_Table(baseTest):

    def test_Tables(self):
        self.home = TestPage(self.driver)
        self.home.click_TableButton()
        time.sleep(2)
        self.home.automate_Table()
        time.sleep(5)
