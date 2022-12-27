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
driver.maximize_window()
driver.get("https://www.google.com/maps/@24.7212962,45.7385594,9z")
searchbox_rest=driver.find_element(By.ID,"searchboxinput")
searchbox_rest.send_keys("indian restaurant in riyadh")
sleep(1)
searchbox_rest.send_keys(Keys.ENTER)
sleep(1)
searchbox_rest.send_keys(Keys.ENTER)
sleep(2)
price='//*[@id="assistive-chips"]/div/div/div/div[1]/div/div/div/div/div[5]/div[2]/div[1]/button'
price_btn=driver.find_element(By.XPATH,price).click()
sleep(2)
cheap="#action-menu > div:nth-child(1)"
cheap_btn=driver.find_element(By.CSS_SELECTOR,cheap)
sleep(1)
moderate="#action-menu > div:nth-child(2)"
moderate_btn=driver.find_element(By.CSS_SELECTOR,moderate)
sleep(1)
clear="//*[@id='action-menu']/div[5]/button[1]"
clear_btn=driver.find_element(By.XPATH,clear)
sleep(1)
from_price =int(input('Enter your price'))
print(from_price)
sleep(1)
if from_price<=40 :
                from_price = int(input('Enter your price '))
                print("cheapest indian restaurant spotted",from_price<=40)
                print(cheap_btn.is_selected())
                cheap_btn.click()
elif from_price>=50:
                from_price=int(input('Enter your price '))
                print("moderate indian restaurant spotted",from_price>=50)
                print(moderate_btn.is_selected())
                moderate_btn.click()
else:
                print("cancel")
                clear_btn.click()
    

        
confirm_price="//*[@id='action-menu']/div[5]/button[2]"
confirm_price_btn=driver.find_element(By.XPATH,confirm_price).click()

        
        
            

