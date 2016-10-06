import os
import time
from selenium import webdriver # to be able to use webdriver service
from selenium.webdriver.common.keys import Keys #Enter much
from chromeservice import chromeService
# username = ""
# pintoken = ''
print("Enter Username:")
username = input()
print("Enter PIN+Token")
pintoken = input()
# get pwd for local urls
dir_path = os.path.dirname(os.path.realpath(__file__))
# define 2fa auth url
auth_url = "file://" + dir_path + "/../simulator/2fa-mockup.html"
# auth_url = "http://ip/"
capabilities = {'browserName':'chrome'}
driverurl = chromeService(status='start')
driver = webdriver.Remote(driverurl, capabilities)
driver.get(auth_url);
assert "Authentication Form" in driver.title # sanity are we in the right page?
userelem = driver.find_element_by_name("DATA")
userelem.clear()
userelem.send_keys(username)
userelem.send_keys(Keys.RETURN)
userelem = driver.find_element_by_name("DATA")
userelem.clear()
userelem.send_keys(pintoken)
userelem.send_keys(Keys.RETURN)
submitelem = driver.find_element_by_name("submit")
submitelem.submit()
time.sleep(1)
chromeService(status='stop')

#