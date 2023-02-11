import pytest
from Config.config import config
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params=[config.browser], scope="class")
def driver_launch(request):
    global s_driver
    if request.param == "chrome":
        s_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = s_driver
    print("-----Test Started-----")
    s_driver.get(config.URL)
    s_driver.implicitly_wait(10)
    yield
    print("----Test Completed----")
    s_driver.quit()

    # how to create class
