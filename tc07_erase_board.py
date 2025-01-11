import time
import unittest
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
time.sleep(1)

#게시판 이동
driver.find_element(By.XPATH, '/html/body/div/header/div/nav/a[2]').click()

#게시판 검색 (데이터 없음)
driver.find_element(By.XPATH, '//*[@id="fTitle"]').send_keys('banana')
driver.find_element(By.CLASS_NAME, 'btn.btn-sm.btn-info.mb-2').click()
time.sleep(1)

#테스트 추출
expected_text = '데이터가 없습니다.'
actual_text = driver.find_element(By.CLASS_NAME, 'text-right').text
print(actual_text)
time.sleep(1)

#Assert 수행
assert expected_text == actual_text , "데이터가 있습니다."

#게시판에 글쓰기
driver.find_element(By.XPATH, '/html/body/div/main/form[2]/div[1]/a').click()
driver.find_element(By.XPATH, '//*[@id="title"]').send_keys('apple3')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="contents"]').send_keys('이 제품은 apple3 입니다.')
time.sleep(1)
driver.find_element(By.CLASS_NAME, 'btn.btn-block.btn-info').click()
time.sleep(6)
#driver.switch_to.alert.accept()
driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[2]/div/a').click()
time.sleep(2)

#게세판 글 삭제하기
driver.find_element(By.XPATH, '/html/body/div/main/form[2]/div[3]/table/tbody/tr[1]/td[1]/div/input').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="delete"]').click()
#파업창 닫기
driver.switch_to.alert.accept()

