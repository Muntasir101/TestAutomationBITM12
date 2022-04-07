import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

class Registration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        cls.driver.get("https://demo.opencart.com/")

    def test_registration_TC001(self):
        self.driver.find_element(By.LINK_TEXT, 'My Account').click()
        self.driver.find_element(By.LINK_TEXT, 'Register').click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
