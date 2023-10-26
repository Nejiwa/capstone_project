import time
from selenium import webdriver

from src.pages.Landing_page import LandingPage

from src.pages.Registration_page import RegPage

from src.pages.Login_page import LoginPage
from src.pages.Product import ProductPage
from src.pages.cart import CartPage
from src.pages.order_page import OrderPage



driver = webdriver.Chrome()
driver.get("http://shop.icraftsoft.net:8095/")

driver.maximize_window()

#Landing_page

lan = LandingPage(driver)
lan.click_login()
time.sleep(10)

# Registration
Reg = RegPage(driver)
Reg.getUsername()
Reg.getEmail()
Reg.getButton()
time.sleep(10)

#Login page
driver.get("http://shop.icraftsoft.net:8095/")
lg = LoginPage(driver)
lg.login_textbox()
time.sleep(2)
lg.click_login()
time.sleep(2)
lg.click_logout()
time.sleep(2)
lg.click_home()
time.sleep(2)
lg.login_textbox2()
time.sleep(2)
lg.login_again()
time.sleep(2)

# Productpage
pro = ProductPage(driver)
pro.search_box()
time.sleep(5)
pro.Quick_view_product()
time.sleep(5)
pro.select_Product1()
time.sleep(5)
pro.Add_to_Cart()
time.sleep(5)
pro.second_cart()
time.sleep(5)

# cartpage
X = CartPage(driver)
X.click_on_cart()
time.sleep(4)

# Orderpage
Ord = OrderPage(driver)
time.sleep(5)
Ord.remove_items()
time.sleep(4)
Ord.continue_shop()
time.sleep(5)
Ord.click_on_cart()
time.sleep(4)
Ord.click_on_Buy_now()
time.sleep(6)
Ord.click_on_home()
time.sleep(5)











