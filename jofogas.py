import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
import openpyxl
import requests
from bs4 import BeautifulSoup

with open(os.path.join(os.path.dirname(__file__), "credentials.txt"), "r") as f:
#with open(r'c:\Users\G\GitHub\01_jofogas\jofogas\credentials.txt', 'r') as f:
    lines=f.readlines()
    for line in lines:
        username=lines[0].strip()
        password=lines[1].strip()

# Browser nyitási feltételek
opt = Options()
opt.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
arr = ['enable-automation', 'disable-popup-blocking', 'disable-notifications']
opt.add_experimental_option("excludeSwitches", arr);
driver = webdriver.Chrome(options=opt, executable_path='c:/webDriver/chromedriver.exe')

###################################################
# Kredentials felolvasás konfig fileból
# Kredentials felolvasása környezeti változóból
# Exception lekezelés

# Weboldalra navigálás
driver.get('https://www.jofogas.hu/')

# maximize the window
driver.maximize_window()

# felugró pop up lekezelése, TAB-al átvált az "elfogadásra és Entert" nyom.
driver.find_element(By.XPATH, '/html/body').send_keys(Keys.TAB + Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER)

time.sleep(2)

# Belépés gombra kattint
driver.find_element(By.XPATH, '//button[text()="Belépés"]').click()

time.sleep(3)

# e-mail cím input mező
driver.find_element(By.ID, "login-modal-email").click()
driver.find_element(By.ID, "login-modal-email").send_keys(username)

# Jelszó input mező
driver.find_element(By.ID, "login-modal-password").click()
driver.find_element(By.ID, "login-modal-password").send_keys(password)

# Belépésre kattintás
driver.find_element(By.ID, "login-modal-submit").click()

time.sleep(5)
# HirdetésFeladás
driver.find_element(By.XPATH, '//*[@id="page-content"]/header/div[3]/div/div[3]/a').click()

# Hirdetés neve
driver.find_element(By.XPATH, '//*[@id="hf_subject"]').click()
driver.find_element(By.XPATH, '//*[@id="hf_subject"]').send_keys("TesztHirdetés")

# Képfeltöltés
path = "D:\\talca.png"
#driver.find_element(By.XPATH, '//*[@id="step1-photo"]/div[3]/div/div[3]/div[2]/label').click() 
#driver.find_element(By.XPATH, '//*[@id="image-uploader-wrapper"]/label').send_keys("D:\\talca.png")
driver.find_element_by_xpath('//*[@id="upload-image"]').send_keys(path)

time.sleep(10)

# Tovább
driver.find_element(By.XPATH, '//*[@id="hirdetesfeladas"]/div/div/button').click()

time.sleep(55)