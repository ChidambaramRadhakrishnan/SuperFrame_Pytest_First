from Page.BaseKeywords import BaseKeywords
from Config.log import log

class windowHandle(BaseKeywords):
    Tabs = "#text=Tabs"
    multiple_window = "#id=multi"

    logger = log.logs()

    def __init__(self, driver):
        super().__init__(driver)

    def click_Tabs(self):
        self.ElementToBeVisible(self.Tabs)
        self.click_On(self.Tabs)

    def click_Multiple_Window(self):
        self.ElementToBeVisible(self.multiple_window)
        self.click_On(self.multiple_window)

    def get_window(self):
        main = self.get_window_Handle()
        return main

    def switch_to_main_window(self, window):
        main_window = self.switch_to_Main_Window(window)
        print(main_window)

    def switch_to_specific_window(self):
        window = self.switch_to_specific_Window("LetCode with Koushik")
        print("Windows has Switched", window)
