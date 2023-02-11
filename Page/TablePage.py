from Page.BaseKeywords import BaseKeywords


class TestPage(BaseKeywords):
    Table = "#text=Simple table"
    Table_data_one = "#xpath=//table[@id='simpletable']//tr/td[1]"

    # Table_Select_opt = "#xpath=//table[@id='simpletable']//tr/td[text()='Koushik']/following-sibling::td[3]"

    def __init__(self, driver):
        super().__init__(driver)

    def click_TableButton(self):
        self.ElementToBeVisible(self.Table)
        self.click_On(self.Table)

    def automate_Table(self):
        self.table_data_select_Some(self.Table_data_one, "Yashwanth")
