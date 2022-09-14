from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 

link = "https://www.instagram.com/p/CiGHLknLJVL/?utm_source=ig_web_copy_link"
username = 'killer_hok_'
password = 'hjmool??'

def start() :
    driver = webdriver.Firefox()
    driver.get('https://instagram.com')
    driver.maximize_window()
    click(driver)
    
    
def click(driver):
    sleep(5)
    user = driver.find_element(By.XPATH, "//input[@name='username']")
    user.send_keys(username)
    
    passw = driver.find_element(By.XPATH, "//input[@name='password']")
    passw.send_keys(password)
    
    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
    sleep(6)
    driver.get(link)
    sleep(5)
    like = driver.find_element(By.XPATH, "//span[@class='_aamw']")
    like.click()
    sleep(5)
    driver.close()
    
start()