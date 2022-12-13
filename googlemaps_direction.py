from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
options=Options()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.google.com/maps/@33.6958321,-7.243721,14z")
searchboxgp=driver.find_element(By.ID,"searchboxinput")
searchboxgp.send_keys("Hayat mall riyadh")
sleep(1)
searchboxgp.send_keys(Keys.ENTER)
sleep(1)
searchboxgp.send_keys(Keys.ENTER)
sleep(1)
direction="/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button"
direction_btn=driver.find_element(By.XPATH,direction).click()
sleep(1)
choice_r1=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/input")
choice_r1.send_keys("northern ring road")
sleep(1)
choice_r1.send_keys(Keys.ENTER)
sleep(1)
choice_r1.send_keys(Keys.ENTER)
sleep(1)
