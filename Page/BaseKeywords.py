from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BaseKeywords:

    def __init__(self, driver):
        self.select = None
        self.driver = driver

    def click_On(self, locator):
        self.ElementToBeClickable(locator)
        print(locator, "....Element has Found")
        self.findElementID(locator).click()

    def customize_Element(self, opt1):
        return self.driver.find_elements(By.XPATH,
                                         "//table[@id='simpletable']//tr/td[text()='" + opt1 + "']/following-sibling::td[3]")

    def findElementID(self, locator):
        if "#id" in locator:
            l = locator[4:]
            while True:
                for x in range(10):
                    if self.driver.find_element(By.ID, l).is_displayed():
                        print("#id=", l, " Element is Looking for.......")
                        return self.driver.find_element(By.ID, l)
        elif "#xpath" in locator:
            l = locator[7:]
            while True:
                for x in range(10):
                    if self.driver.find_element(By.XPATH, l).is_displayed():
                        print("#xpath=", l, " Element is Looking for........")
                        return self.driver.find_element(By.XPATH, l)
        elif "#text" in locator:
            l = locator[6:]
            while True:
                for x in range(10):
                    if self.driver.find_element(By.LINK_TEXT, l).is_displayed():
                        print("#text=", l, " Element is Looking for........")
                        return self.driver.find_element(By.LINK_TEXT, l)

    def findElements(self, locator):
        if "#id" in locator:
            l = locator[4:]
            while True:
                for x in range(10):
                    print("#id=", l, " Element is Looking for.......")
                    return self.driver.find_elements(By.ID, l)
        elif "#xpath" in locator:
            l = locator[7:]
            while True:
                for x in range(10):
                    print("#xpath=", l, " Element is Looking for........")
                    return self.driver.find_elements(By.XPATH, l)
        elif "#text" in locator:
            l = locator[6:]
            while True:
                for x in range(10):
                    print("#text=", l, " Element is Looking for........")
                    return self.driver.find_elements(By.LINK_TEXT, l)

    # self.driver.find_element(By.XPATH, locator).click()

    def getTitle(self):
        title = self.driver.title
        print(title)
        return title

    def Wait(self):
        wait = WebDriverWait(self.driver, 5)
        return wait

    def ElementToBeClickable(self, locator):
        self.Wait().until(ec.element_to_be_clickable(self.findElementID(locator)))

    def ElementToBeVisible(self, locator):
        self.Wait().until(ec.visibility_of(self.findElementID(locator)))

    def send_keys(self, locator, Keys):
        self.ElementToBeClickable(locator)
        print(locator, "....Element has Found")
        self.findElementID(locator).send_keys(Keys)
        return self.findElementID(locator).get_attribute("value")

    def select_option_dropdown(self, locator, options):
        # self.ElementToBeClickable(locator)
        self.ElementToBeClickable(locator)
        print(locator, "....Element has Found")
        self.select = Select(self.findElementID(locator))
        self.select.select_by_visible_text(options)
        option = self.select.first_selected_option
        print(option)

    # except "ElementNotSelectableException":
    #     throw_error("ElementNotSelectableException")

    def get_window_Handle(self):
        main = self.driver.current_window_handle
        return main

    def switch_to_Main_Window(self, window):
        self.driver.switch_to.window(window)
        return self.driver.title

    def switch_to_specific_Window(self, title):
        handles = self.driver.window_handles
        for window in handles:
            if title in self.driver.title:
                self.driver.switch_to.window(window)
        return self.driver.title

    def table_data_select_Some(self, locator1, opt):
        for x in self.findElements(locator1):
            texts = x.text
            if opt in texts:
                e = self.driver.find_element(By.XPATH,
                                             "//table[@id='simpletable']//tr/td[text()='" + opt + "']/following::input")
                e.click()
