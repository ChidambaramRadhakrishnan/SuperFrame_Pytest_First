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
    s_driver.get(config.URL)
    s_driver.implicitly_wait(10)
    yield
    s_driver.quit()




