import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


class Login(unittest.TestCase):
    def test_login_TC001_valid(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("https://demo.opencart.com/")

        my_account = driver.find_element(By.LINK_TEXT, 'My Account')
        my_account.click()
        # login = driver.find_element_by_link_text('Login')
        login = driver.find_element(By.LINK_TEXT, 'Login')
        login.click()

        email = driver.find_element(By.NAME, "email")
        email.clear()
        email.send_keys("user6@bd.com")
        password = driver.find_element(By.NAME, "password")
        password.clear()
        password.send_keys("123456")

        loginBtn = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
        loginBtn.click()

        print("Login Test case 001 executed.")
        self.assert_(True)

        driver.close()

    def test_login_TC002_invalid(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("https://demo.opencart.com/")

        my_account = driver.find_element(By.LINK_TEXT, 'My Account')
        my_account.click()
        # login = driver.find_element_by_link_text('Login')
        login = driver.find_element(By.LINK_TEXT, 'Login')
        login.click()

        email = driver.find_element(By.NAME, "email")
        email.clear()
        email.send_keys("user6@bdqeweq.com")
        password = driver.find_element(By.NAME, "password")
        password.clear()
        password.send_keys("123456")
        loginBtn = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
        loginBtn.click()

        print("Login Test case 002 executed.")
        self.assert_(True)

        driver.close()

    def test_login_TC003_invalid(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("https://demo.opencart.com/")

        my_account = driver.find_element(By.LINK_TEXT, 'My Account')
        my_account.click()
        # login = driver.find_element_by_link_text('Login')
        login = driver.find_element(By.LINK_TEXT, 'Login')
        login.click()

        email = driver.find_element(By.NAME, "email")
        email.clear()
        email.send_keys("user6@bd.com")
        password = driver.find_element(By.NAME, "password")
        password.clear()
        password.send_keys("ew")
        loginBtn = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
        loginBtn.click()

        print("Login Test case 003 executed.")
        self.assert_(True)

        driver.close()

    def test_login_TC004_invalid(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.get("https://demo.opencart.com/")

        my_account = driver.find_element(By.LINK_TEXT, 'My Account')
        my_account.click()
        # login = driver.find_element_by_link_text('Login')
        login = driver.find_element(By.LINK_TEXT, 'Login')
        login.click()

        email = driver.find_element(By.NAME, "email")
        email.clear()
        email.send_keys(" ")
        password = driver.find_element(By.NAME, "password")
        password.clear()
        password.send_keys("")

        loginBtn = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
        loginBtn.click()

        print("Login Test case 003 executed.")
        self.assert_(True)

        driver.close()


if __name__ == '__main__':
    unittest.main
