from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

s = Service("chromedriver.exe")
options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("start-maximized")

#브라우저 열기
driver = webdriver.Chrome(service=s, options=options)

#테스트 대상 열기
url = "http://127.0.0.1:8080"
driver.get(url)

#로그인 정보
id = 'admin'
pw = 'admin'
xpaths={'id':'//*[@id="username"]','pw':'//*[@id="inputPassword"]'}

#로그인 정보 넣기
driver.find_element(By.XPATH, xpaths['id']).send_keys(id)
driver.find_element(By.XPATH, xpaths['pw']).send_keys(pw)
 
#로그인 하기
driver.find_element(By.XPATH, '/html/body/form/button').click()