from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


driver.get("https://www.cssscript.com/demo/multiselect-dropdown-list-checkboxes-multiselect-js/")
dropdown = driver.find_element(By.XPATH, '//*[@id="testSelect1_input"]')

options = Select(dropdown)

options.deselect_by_value('Item 1')