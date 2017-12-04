from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
driver = webdriver.Chrome('D:\\chromedriver.exe')
driver.get("http://photobuzzz.herokuapp.com");
time.sleep(2);
userName = driver.find_element_by_name("username")
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
    print("Test Fail!!!!")
    driver.close();
try:
    edit = driver.find_element_by_xpath("//a[text()='edit your profile']")
    if edit.is_displayed():
        edit.click();
        print("Edit profile clicked!")
except NoSuchElementException:
    print("Could not find the edit profile link")
    driver.close();
driver.find_element_by_name("first_name").clear();
driver.find_element_by_name("first_name").send_keys("Aksh");
driver.find_element_by_name("last_name").clear();
driver.find_element_by_name("last_name").send_keys("Sr");
driver.find_element_by_name("email").clear();
driver.find_element_by_name("email").send_keys("akshitha82@yahoo.com");
driver.find_element_by_name("date_of_birth").clear();
driver.find_element_by_name("date_of_birth").send_keys("12/12/1992");
time.sleep(2);
driver.find_element_by_xpath("//input[@value='Save changes']").click();
time.sleep(2);
try:
    update = driver.find_element_by_xpath("//li[@class='success']")
    if update.is_displayed():
        update.click();
        print("Successfully edited profile")
        print("Test Pass!!!")
except NoSuchElementException:
    print("Could not edit profile")
    print("Test Fail!!!")
    driver.close();
driver.close();