import os
from selenium import webdriver # to be able to use webdriver service
from chromeservice import chromeservice
# get pwd for local urls
dir_path = os.path.dirname(os.path.realpath(__file__))
# define 2fa auth url
auth_url = "file://" + dir_path + "/../simulator/2fa-mockup.html"
# auth_url = "http://ip/"
capabilities = {'browserName':'chrome'}
driverurl = chromeservice(status='start')
driver = webdriver.Remote(driverurl, capabilities)
driver.get(auth_url);

chromeservice(status='stop')

#