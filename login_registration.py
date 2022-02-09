import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#регистрация аккаунта
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
account = driver.find_element_by_id("menu-item-50").click()
email = driver.find_element_by_id("reg_email")
email.send_keys("a11@r.ru")
password = driver.find_element_by_id("reg_password")
password.send_keys("ZzXxCc11")
register_btn = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".woocomerce-FormRow.form-row :nth-child(3)"))).click()
driver.quit()

#логин в систему
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
account = driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("a11@r.ru")
password_user = driver.find_element_by_id("password")
password_user.send_keys("ZzXxCc11")
login_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='login']"))).click()
logout = driver.find_element_by_css_selector(".woocommerce-MyAccount-navigation :nth-child(6) >a")
logout_get_text = logout.text
assert logout_get_text == "Logout"
if driver.find_element_by_css_selector('.woocommerce-MyAccount-navigation :nth-child(6) >a'):
    print ("Element exists")
driver.quit()



