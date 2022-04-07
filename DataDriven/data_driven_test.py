from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from DataDriven import excel_utils

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://demo.opencart.com/")
my_account = driver.find_element(By.LINK_TEXT, 'My Account')
my_account.click()
login = driver.find_element(By.LINK_TEXT, 'Login')
login.click()

login_data_file = 'Login_data.xlsx'
login_sheet_invalid = 'Login_invalid'
login_sheet_valid = 'Login_valid'
number_of_rows = excel_utils.get_row_count(login_data_file, login_sheet_valid)
number_of_columns = excel_utils.get_column_count(login_data_file, login_sheet_valid)

for r in range(2, number_of_rows + 1):
    dd_email = excel_utils.read_data(login_data_file, login_sheet_valid, r, 1)
    dd_password = excel_utils.read_data(login_data_file, login_sheet_valid, r, 2)

    email = driver.find_element(By.NAME, "email")
    email.clear()
    email.send_keys(dd_email)
    password = driver.find_element(By.NAME, "password")
    password.clear()
    password.send_keys(dd_password)

    loginBtn = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
    loginBtn.click()

    if driver.title == 'My Account':
        excel_utils.write_data(login_data_file, login_sheet_valid, r, 3, "Login Success.Test passed")
    else:
        excel_utils.write_data(login_data_file, login_sheet_valid, r, 3, "Didn't LoginTest Failed.")


driver.close()