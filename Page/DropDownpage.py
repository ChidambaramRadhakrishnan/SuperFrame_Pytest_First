from Config.config_data import data
from Page.BaseKeywords import BaseKeywords


class dropdown_Page(BaseKeywords):
    select_btn = "#text=Drop-Down"
    select_dropdown_opt = "#id=fruits"
    select_dropdown = "#xpath=//div[@class='select']//select[@id='fruits']"

    def __init(self, driver):
        super().__init__(driver)

    def click_Select_Button(self):
        self.click_On(self.select_btn)

    def get_Title(self):
        print(self.getTitle())

    def click_dropdown(self):
        self.click_On(self.select_dropdown)

    def select_dropdowns(self):
        self.select_option_dropdown(self.select_dropdown_opt, "Orange")

