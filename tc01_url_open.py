from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

#116.0.5845.141
s = Service("chromedriver.exe")

options = Options()
options.add_experimental_option("detach", True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=s, options=options)

url = "http://127.0.0.1:8080"
driver.get(url)