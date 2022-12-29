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
searchbox_rest.send_keys("fried chicken restaurants in riyadh")
sleep(1)
searchbox_rest.send_keys(Keys.ENTER)
sleep(3)
searchbox_rest.send_keys(Keys.ENTER)
sleep(4)
rating='//*[@id="assistive-chips"]/div/div/div/div[1]/div/div/div/div/div[5]/div[2]/div[2]/button'
rating_btn=driver.find_element(By.XPATH,rating).click()
sleep(5)
rating1="#action-menu > div:nth-child(2)"
rating_2stars=driver.find_element(By.CSS_SELECTOR,rating1)
sleep(3)
rating2="#action-menu > div:nth-child(3)"
rating_2half=driver.find_element(By.CSS_SELECTOR,rating2)
sleep(4)
rating3="#action-menu > div:nth-child(4)"
rating_3stars=driver.find_element(By.CSS_SELECTOR,rating3)
sleep(5)
rating4="#action-menu > div:nth-child(5)"
rating_3half=driver.find_element(By.CSS_SELECTOR,rating4)
sleep(4)
from_rating=float(input('rate the fried chicken restaurants in riyadh city:'))
print(from_rating)
sleep(3)
if from_rating==2.0:
    from_rating = float(input('rate the fried chicken restaurants in riyadh city'))
    print("fried chicken restaurant with two stars spotted")
    print(rating_2stars.is_selected())
    rating_2stars.click()   
elif from_rating==2.5:
    from_rating = float(input('rate the fried chicken restaurants in riyadh city'))
    print("fried chicken restaurant with two stars and half stars spotted",from_rating==2.5)
    print(rating_2half.is_selected())
    rating_2half.click()  
    
elif from_rating==3.0:
      from_rating = float(input('rate the fried chicken restaurants in riyadh city:'))
      print("fried chicken restaurants with three stars spotted",from_rating==3.0)
      print(rating_3stars.is_selected())
      rating_3stars.click()
elif from_rating==3.5:
    from_rating = float(input('rate the fried chicken restaurants in riyadh city:'))
    print("fried chicken restaurants with three stars and half spotted",from_rating==3.5)
    print(rating_3half.is_selected())
    rating_3half.click()
      
               

else:
                driver.quit()
