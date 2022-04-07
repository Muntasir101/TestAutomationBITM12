from behave import *
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


@given(u'I launched firefox')
def step_implementation(context):
    context.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

@when(u'I open login page')
def step_implementation(context):
    context.driver.get("https://demo.opencart.com/index.php?route=account/account")

@when(u'I enter email')
def step_implementation(context):
    context.driver.find_element(By.NAME, "email").send_keys('user101@gmail.com')

@when(u'I enter password')
def step_implementation(context):
    context.driver.find_element(By.NAME, "password").send_keys('123456')

@when(u'I click login')
def step_implementation(context):
    context.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input').click()

@then(u'Login successful')
def step_implementation(context):
    if context.driver.title == 'My Account':
        print("Login successful")
    else:
        print("Login Failed")

    context.driver.close()
