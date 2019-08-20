import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

caps=DesiredCapabilities.FIREFOX
caps['binary']="D:\firefox\firefox.exe"
browser = webdriver.Firefox(capabilities=caps,executable_path="C:\\Users\\dzy95\\Downloads\\geckodriver.exe")
browser.get('')