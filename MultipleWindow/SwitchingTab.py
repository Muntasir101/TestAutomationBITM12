from selenium import webdriver

from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

driver.get('https://the-internet.herokuapp.com/windows')

parent_GUID = driver.current_window_handle
# print(parent_GUID)

driver.find_element(By.LINK_TEXT, 'Click Here').click()
all_GUID = driver.window_handles
# print(all_GUID)
# print(len(all_GUID))

# Switch to Child
for child_GUID in all_GUID:
    if child_GUID != parent_GUID:
        driver.switch_to.window(child_GUID)
        driver.get("https://google.com")
        print('Child window Title :' + driver.title)

# Back to parent
driver.switch_to.window(parent_GUID)
print('parent Window Title :' + driver.title)

# Switch to Child
for child_GUID in all_GUID:
    if child_GUID != parent_GUID:
        driver.switch_to.window(child_GUID)
        driver.get("https://demo.opencart.com/")
        print('Child window Title :' + driver.title)


# Back to parent
driver.switch_to.window(parent_GUID)
print('parent Window Title :' + driver.title)

driver.quit()





