import logging
from asyncio import sleep

from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# from seleyasha.browser import Browser
from orangeTest.conditions import element, type, click, find_element
from orangeTest.pages.login_page import LoginPage

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, timeout=2, ignored_exceptions=(WebDriverException,))
# 2
# browser = Browser(driver)
login_page = LoginPage()
driver.get('https://opensource-demo.orangehrmlive.com/')
# 2
# browser.open('https://ecosia.org')

'''
# in Selene:
browser.element('[name=q]').type('selene').press_enter()
# in Selenium WebDriver:
driver.find_element(By.CSS_SELECTOR, '[name=q]').send_keys('selene', Keys.ENTER)
# OR with wait
def find_element(driver):
    return driver.find_element(By.CSS_SELECTOR, '[name=q]')
wait.until(find_element).send_keys('selene', Keys.ENTER)
# OR with built-in expected condition
wait.until(visibility_of_element_located((By.NAME, 'q'))).send_keys('selene yashaka', Keys.ENTER)
# OR with custom expected condition
wait.until(element('[name=q]')).send_keys('selene yashaka', Keys.ENTER)
'''

# query = '[name=q]'
# wait.until(type(query, value='selene' + Keys.ENTER))

# wait.until(visibility_of_element_located((By.CSS_SELECTOR, 'input[name*="username"]'))).send_keys('random_name', Keys.ENTER)
# wait.until(type('input[name*="username"]', value='random_name'))
wait.until(login_page.fill_username("random name"))

# wait.until(visibility_of_element_located((By.CSS_SELECTOR, 'input[name*="password"]'))).send_keys('random_pass', Keys.ENTER)
wait.until(type('input[name*="password"]', value='random_pass'))

wait.until(click('button[type*="submit"]'))
# wait.until(visibility_of_element_located((By.XPATH_SELECTOR, '//p[.="Invalid credentials"]')))
# wait.until(element('//p[.="Invalid credentials"]', value='random_pass' + Keys.ENTER))
wait.until(element('//p[.="Invalid credentials"]'))

# driver.get('https://opensource-demo.orangehrmlive.com/')
driver.back()
username = wait.until(find_element('//div[contains(@class,"demo-credentials")]/p[1]'))
username = username.text
username = username.split(": ")[1]
print(username)

password = wait.until(find_element('//div[contains(@class,"demo-credentials")]/p[2]'))
password = password.text
password = password.split(": ")[1]
print(password)

wait.until(type('input[name*="username"]', value=username))
wait.until(type('input[name*="password"]', value=password))
wait.until(click('button[type*="submit"]'))
#
wait.until(element('//div[contains(@class,"userarea")]//p[.="Paul Collings"]'))
logging.info("Paul Collings")

# //div[contains(@class,'userarea')]//p[.="Paul Collings"]

# 1
# type('[name=q]', value='selene' + Keys.ENTER)
# 2
# browser.type('[name=q]', value='selene' + Keys.ENTER)
# 3
# element('[name=q]').type('selene' + Keys.ENTER)
# ...
# query = element('[name=q]')
# query.type('selene' + Keys.ENTER)

# driver.back()

# wait.until(type(query, value=' yashaka' + Keys.ENTER))
# # 1
# # type(query, ' yashaka' + Keys.ENTER)
# # 2
# # browser.type(query, ' yashaka' + Keys.ENTER)
# # 3
# # query.type(' yashaka' + Keys.ENTER)
#
# wait.until(click('[data-test-id=mainline-result-web]:nth-of-type(1) a'))
# # 1
# # click('[data-test-id=mainline-result-web]:nth-of-type(1) a')
# # 2
# # browser.click('[data-test-id=mainline-result-web]:nth-of-type(1) a')
#
# wait.until(click('[data-test-id=mainline-result-web]:nth-of-type(1) a'))
# # 1
# # click('[data-test-id=mainline-result-web]:nth-of-type(1) a')
# # 2
# # browser.click('[data-test-id=mainline-result-web]:nth-of-type(1) a')
#
# wait.until(number_of_elements('[id^=issue_]:not([id$=_link])', value=4))
# 1
# assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', value=4))
# 2
# browser.assert_that(number_of_elements('[id^=issue_]:not([id$=_link])', value=4))
'''
# less stable version:
number_of_pulls = len(driver.find_elements(By.CSS_SELECTOR, '[id^=issue_]:not([id$=_link])'))
assert number_of_pulls == 4
'''
