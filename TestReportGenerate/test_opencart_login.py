import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        cls.driver.get("https://demo.opencart.com/index.php?route=account/login")

    def test_login_TC001_valid(self):
        self.driver.find_element(By.NAME, "email").clear()
        self.driver.find_element(By.NAME, "email").send_keys("user6@bd.com")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys('1234556')
        self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input').click()

        print("Login Test case 001 executed.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
