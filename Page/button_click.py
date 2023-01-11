from tqdm import tk

from Page.BaseKeywords import BaseKeywords


class click_Btn(BaseKeywords):
    click_Btn = "#Text=Click"
    click_goToBtn = "#id=home"

    def __init__(self, driver):
        super().__init__(driver)

    def get_Title(self):
        self.getTitle()

    def click_btn(self):
        self.click_OnText(self.click_Btn)

    def click_goto_Home(self):
        self.click_OnText(self.click_goToBtn)
