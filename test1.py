import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

caps=DesiredCapabilities.FIREFOX
caps['binary']="D:\firefox\firefox.exe"
browser = webdriver.Firefox(capabilities=caps,executable_path="C:\\Users\\dzy95\\Downloads\\geckodriver.exe")
browser.get("http://www.google.ca")
print(browser.title)
print(browser.current_url)
browser.find_element_by_name('q').send_keys('python')
browser.find_element_by_css_selector("html body#gsr.hp.vasq.big div#viewport.ctr-p div#searchform.jhp.big form#tsf.tsf.nj div div.A8SBwf div.FPdoLc.VlcLAe center input.gNO89b").click()
ele1=browser.find_element_by_xpath("/html/body/div[6]/div[3]/div[10]/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div/div[1]/a[1]/h3")
ActionChains(browser).context_click(ele1).perform()
browser.find_element_by_name('q').send_keys(Keys.CONTROL,'a')
browser.implicitly_wait(3)
browser.find_element_by_name('q').send_keys(Keys.CONTROL,'x')
time.sleep(1)
browser.find_element_by_name('q').send_keys(Keys.CONTROL,'v')
time.sleep(1)
browser.find_element_by_name('q').send_keys(Keys.ENTER)
time.sleep(3)
browser.quit()