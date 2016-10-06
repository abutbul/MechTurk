# this control script crontrols chromium driver service for calls
# usage: include us and selenium webdriver
# from selenium import webdriver
# from chromeservice import chromeservice
# get service url by activating service chromeservice('start')
# control chrome with webdriver.remote. consult documentation: https://sites.google.com/a/chromium.org/chromedriver/
# do not remove import for service from this file! altough parser may cry, it is used when called.
import selenium.webdriver.chrome.service as service

def chromeservice(status): # my first python service :)
    if status in ['start', 1]: # found out python doesn't like case/switch
        global service # this is almost voodoo still learning I guess
        service = service.Service('/usr/lib/chromium-browser/chromedriver')
        service.start()
        global_service_url = service.service_url
        return global_service_url # this defines usage, could be probably done better. TODO
    elif status in ['stop', 0]:
        service.stop()
    else:
        print("unknown service call")

# testing grounds
# service = service.Service('/usr/lib/chromium-browser/chromedriver')
# chromeservice('start')
# capabilities = {'browserName':'chrome'}
# driver = webdriver.Remote(service.service_url, capabilities)
# driver.get('http://www.google.com/xhtml');
# chromeservice('stop')
