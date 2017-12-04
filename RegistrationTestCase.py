from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome('D:\\chromedriver.exe')
driver.get("http://photobuzzz.herokuapp.com");
time.sleep(2);
driver.find_element_by_xpath("//a[text()='register here']").click();
time.sleep(1);
userName = driver.find_element_by_name("username");
userName.send_keys("test12");
firstName = driver.find_element_by_name("first_name");
firstName.send_keys("Test12");
email = driver.find_element_by_name("email");
email.send_keys("test12@test.com");
passWord = driver.find_element_by_name("password");
passWord.send_keys("test12");
confirmpassWord = driver.find_element_by_name("password2");
confirmpassWord.send_keys("test12");
time.sleep(2);
driver.find_element_by_xpath("//input[@type='submit']").click();
time.sleep(2);
try:
    elem = driver.find_element_by_xpath("//h1[text()='Welcome Test12!']")
    if elem.is_displayed():
        elem.click();
        print("Account successfully registered!")
except NoSuchElementException:
    print("Account could not be registered, Test Fail!!")
driver.find_element_by_xpath("//a[text()='log in']").click();
time.sleep(2);
try:
    elem = driver.find_element_by_xpath("//h1[text()='Log-in']")
    if elem.is_displayed():
        elem.click();
        print("Log in page is displayed!")
except NoSuchElementException:
    print("Log in page is not displayed!, Test Fail!!")
uname = driver.find_element_by_name("username");
uname.send_keys("test12");
pwd = driver.find_element_by_name("password");
pwd.send_keys("test12");
driver.find_element_by_xpath("//input[@value='Log-in']").click();
time.sleep(2);
try:
    elem = driver.find_element_by_xpath("//h1[text()='Dashboard']")
    if elem.is_displayed():
        elem.click();
        print("Dashboard is displayed!")
        print("Test Pass!")
except NoSuchElementException:
    print("Dashboard is not displayed")
    print("Test Fail!!!!")
driver.find_element_by_link_text("Logout").click();
driver.close();
