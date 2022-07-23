import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import openpyxl
import requests
from bs4 import BeautifulSoup


opt = Options()
opt.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
arr = ['enable-automation', 'disable-popup-blocking', 'disable-notifications']
opt.add_experimental_option("excludeSwitches", arr);
driver = webdriver.Chrome(
    options=opt, executable_path='c:/webDriver/chromedriver.exe')
driver.get('https://www.jofogas.hu/')

time.sleep(2)

driver.find_element_by_xpath('//*[@id="didomi-notice-agree-button"]/span').sendKeys("TAB")

#sendKeys("TAB")
#sendKeys("TAB")

#switch = driver.switch_to.alert.sendKeys("TAB") 
#driver.switchTo().alert().sendKeys("TAB");
driver.find_element_by_xpath('//*[@id="didomi-notice-agree-button"]/span').click()
