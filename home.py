import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Добавление комментария
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
read_more_btn = driver.find_element_by_xpath("//img[@title='Selenium Ruby']//..//..//h3").click()
reviews_btn = driver.find_element_by_class_name("reviews_tab").click()
star = driver.find_element_by_class_name("star-5").click()
reviewtext = driver.find_element_by_id("comment")
reviewtext.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("user")
email =driver.find_element_by_id("email")
email.send_keys("user@ya.ru")
submit_btn =driver.find_element_by_id("submit").click()
driver.quit()
