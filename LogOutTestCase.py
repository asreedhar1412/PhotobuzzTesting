from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome('D:\\chromedriver.exe');
driver.get("http://photobuzzz.herokuapp.com");
time.sleep(2);
userName = driver.find_element_by_name("username");
userName.send_keys("akshi");
passWord = driver.find_element_by_name("password");
passWord.send_keys("zxcv@098Z");
driver.find_element_by_xpath("//input[@value='Log-in']").click();
time.sleep(4);
try:
    elem = driver.find_element_by_xpath("//h1[text()='Dashboard']")
    if elem.is_displayed():
        elem.click();
        print("Dashboard is displayed!")
except NoSuchElementException:
    print("Dashboard is not displayed")
try:
    elem1 = driver.find_element_by_link_text("Logout")
    if elem1.is_displayed():
        elem1.click();
        print("Successfully Logged Out, Test Pass!")
except NoSuchElementException:
    print("Could not log out, Test Fail!")
time.sleep(2);
driver.close();