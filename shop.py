import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://practice.automationtesting.in/")
account = driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("a11@r.ru")
password_user = driver.find_element_by_id("password")
password_user.send_keys("ZzXxCc11")
login_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='login']"))).click()
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
html5 = driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']").click()
title = driver.find_element_by_css_selector(".product_title.entry-title")
title_get_text = title.text
if title_get_text == "HTML5 Forms":
    print("yes")
else:
    print("null")
#или
    #title_get_text = title.text
    #assert title_get_text == "HTML5 Forms"
driver.quit()

# количество товаров в категории
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://practice.automationtesting.in/")
account = driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("a11@r.ru")
password_user = driver.find_element_by_id("password")
password_user.send_keys("ZzXxCc11")
login_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='login']"))).click()
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
html_btn = driver.find_element_by_css_selector(".cat-item-19>a").click()
htmlcateg = driver.find_element_by_css_selector(".cat-item-19>span")
htmlcateg_get_text = htmlcateg.text
assert htmlcateg_get_text == "(3)"
if driver.find_elements_by_css_selector('.product.type-product'):
    print ("Element exists")
driver.quit()


# сортировка товаров
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://practice.automationtesting.in/")
account = driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("a11@r.ru")
password_user = driver.find_element_by_id("password")
password_user.send_keys("ZzXxCc11")
login_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='login']"))).click()
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
selector = driver.find_element_by_css_selector(".orderby")
selector_check = selector.get_attribute("value")
if selector_check == "menu_order":
   print(selector_check)
else:
  print("null")
selectSort = Select(driver.find_element_by_css_selector(".orderby"))
selectSort.select_by_index(5)
selector1 = driver.find_element_by_css_selector(".orderby")
selector_check1 = selector1.get_attribute("value")
if selector_check1 == "price-desc":
    print (selector_check1)
else:
    print("null")
driver.quit()

# отображение, скидка товара
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://practice.automationtesting.in/")
account = driver.find_element_by_id("menu-item-50").click()
username = driver.find_element_by_id("username")
username.send_keys("a11@r.ru")
password_user = driver.find_element_by_id("password")
password_user.send_keys("ZzXxCc11")
login_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name='login']"))).click()
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
android_book = driver.find_element_by_css_selector("[title='Android Quick Start Guide']").click()
price_old = driver.find_element_by_css_selector(".price>del")
price_old_get_text = price_old.text
assert "600.00" in price_old_get_text
price_new = driver.find_element_by_css_selector(".price>ins")
price_new_get_text = price_new.text
assert "450.00" in price_new_get_text
Img = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Android Quick Start Guide']")) ).click()
Img_close = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")) ).click()
driver.quit()

# проверка цены в корзине
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://practice.automationtesting.in/")
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
driver.execute_script("window.scrollBy(0, 600);")
html5web_book = driver.find_element_by_xpath("//*[@id='content']/ul/li[4]/a[2]").click()
time.sleep(10)
basket = driver.find_element_by_css_selector(".cartcontents")
basket_get_text = basket.text
assert "1 Item" in basket_get_text
basket_cost =driver.find_element_by_css_selector(".wpmenucart-contents :nth-child(3)")
basket_cost_get_text = basket_cost.text
assert "₹180.00" in basket_cost_get_text
basket_btn = driver.find_element_by_css_selector(".wpmenucart-contents").click()
subtotal = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.XPATH, "//div[@class='cart_totals ']//td[@data-title='Subtotal']//span"), "180"))
Total = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='cart_totals ']//td[@data-title='Total']//span"), "189"))
driver.quit()

# работа в корзине
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://practice.automationtesting.in/")
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
driver.execute_script("window.scrollBy(0, 300);")
html5web_book = driver.find_element_by_xpath("//*[@id='content']/ul/li[4]/a[2]").click()
time.sleep(5)
JS_book = driver.find_element_by_xpath("//*[@id='content']/ul/li[5]/a[2]").click()
time.sleep(5)
basket = driver.find_element_by_css_selector(".cartcontents").click()
time.sleep(10)
html5web_bookDel = driver.find_element_by_xpath("//*[@id='page-34']//tr[1]/td[1]/a").click()
time.sleep(10)
Undo = driver.find_element_by_css_selector(".woocommerce-message>a")
driver.execute_script("arguments[0].click();", Undo)
quatityJS = driver.find_element_by_xpath("//*[@id='page-34']//tr[1]/td[5]//input").clear()
quatityJS = driver.find_element_by_xpath("//*[@id='page-34']//tr[1]/td[5]//input")
quatityJS.send_keys("3")
Update_basket = driver.find_element_by_css_selector(".actions>input[type=submit]").click()
time.sleep(10)
quatityJS = driver.find_element_by_xpath("//*[@id='page-34']//tr[1]/td[5]//input")
quatityJS_check = quatityJS.get_attribute("value")
print(quatityJS_check)
assert quatityJS_check == "3"
time.sleep(10)
Apply_coupon = driver.find_element_by_css_selector(".coupon>input[type=submit]").click()
time.sleep(5)
messagetable = driver.find_element_by_css_selector('.woocommerce-error>li')
messagetable_get_text = messagetable.text
print(messagetable_get_text)
assert messagetable_get_text == "Please enter a coupon code."
driver.quit()

# покупка товара
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://practice.automationtesting.in/")
shop_btn = driver.find_element_by_css_selector("#menu-item-40>a").click()
driver.execute_script("window.scrollBy(0, 300);")
html5web_book = driver.find_element_by_xpath("//*[@id='content']/ul/li[4]/a[2]").click()
time.sleep(5)
basket = driver.find_element_by_css_selector(".cartcontents").click()
proceed_btn = WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout>a"))).click()
firstname =  WebDriverWait(driver, 15).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name")) )
firstname.send_keys("user1")
Lastname = driver.find_element_by_id("billing_last_name")
Lastname.send_keys("user2")
Email = driver.find_element_by_id("billing_email")
Email.send_keys("user@ya.ru")
Phone = driver.find_element_by_id("billing_phone")
Phone.send_keys("89999999999")
country = driver.find_element_by_id("s2id_billing_country").click()
country_input = driver.find_element_by_id("s2id_autogen1_search")
country_input.send_keys("Russia")
Russia = driver.find_element_by_css_selector(".select2-match").click()
Address = driver.find_element_by_css_selector("input[name=billing_address_1]")
Address.send_keys("xxxx")
City = driver.find_element_by_id("billing_city")
City.send_keys("Moscow")
County = driver.find_element_by_id("billing_state")
County.send_keys("-")
Postcode = driver.find_element_by_id("billing_postcode")
Postcode.send_keys("1234567")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
CheckPay = driver.find_element_by_css_selector("input[value=cheque]").click()
Place_order_btn = driver.find_element_by_id("place_order").click()
Text = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.XPATH, "//*[@id='page-35']//div//p[1]"), "Thank you. Your order has been received."))
Payment_method = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.XPATH, "//*[@id='page-35']//div//tr[3]//td"), "Check Payments"))
print(Payment_method)
driver.quit()





