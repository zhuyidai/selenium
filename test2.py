from selenium import webdriver
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from userdata1 import get_webinfo, get_userinfo
from logtest import Loginfo


def get_time(driver, times, func):
    return WebDriverWait(driver, times).until(func)


def open_browser():
    caps = DesiredCapabilities.FIREFOX
    caps['binary'] = "D:\firefox\firefox.exe"
    webdriver_handle=webdriver.Firefox(capabilities=caps,executable_path="C:\\Users\\dzy95\\Downloads\\geckodriver.exe")
    return webdriver_handle


def load_url(browser, url):
    browser.get(url)
    browser.maximize_window()
    browser.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[2]/div/a[2]/span[1]').click()


def find_ele(browser,arg):

    userele=browser.find_element_by_id(arg['userid'])
    pwdele=browser.find_element_by_id(arg['pwdid'])
    loginele=browser.find_element_by_id(arg['login1'])
    return userele, pwdele, loginele


def sendVals(eletuple,arg):
        listkey=['uname', 'pwd']
        i=0
        for key in listkey:
            eletuple[i].send_keys(arg[key])
            i+=1
        eletuple[2].click()


def checkresult(browser,err_path,arg,log):
    result=False
    time.sleep(2)
    try:
        err = browser.find_element_by_xpath(err_path)
        print('wrong')
        msg='%s: error: %s' % (arg['uname'],arg['pwd'],err.text)
        log.log_write(msg)

    except:
        result = True
        msg ='%s: pass %s\n'%(arg['uname'],arg['pwd'])
        log.log_write(msg)
    return result


def logout(browser,ele_dict):
    


def login_test(ele_dict, user_list):
    browser = open_browser()
    log= Loginfo()
    load_url(browser, url)
    ele_tuple=find_ele(browser,ele_dict)
    for arg in user_list:
        sendVals(ele_tuple,arg)
        time.sleep(2)
        result= checkresult(browser,ele_dict['err_path'],arg,log)
        #if result:
            #log out
            #log in
    log.log_close()
url="http://www.amazon.ca"
account='daizhuyi999@gmail.com'
pwd='dzy6139790773!!'
'''
ele_dict={'url':url,'userid':'ap_email', 'pwdid':'ap_password','login1':'signInSubmit','uname':account,'pwd':pwd}
user_list=[{'uname':account,'pwd':pwd}]
'''
ele_dict=get_webinfo(r'D:\BaiduNetdiskDownload\webinfo.txt')
user_list=get_userinfo(r'D:\BaiduNetdiskDownload\userinfo.txt')
login_test(ele_dict,user_list)