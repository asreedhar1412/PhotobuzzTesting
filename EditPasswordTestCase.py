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
    driver.close();
try:
    edit = driver.find_element_by_xpath("//a[text()='change your password']")
    if edit.is_displayed():
        edit.click();
        print("Change password clicked!")
except NoSuchElementException:
    print("Could not find the change password link")
    driver.close();
driver.find_element_by_name("old_password").clear();
driver.find_element_by_name("old_password").send_keys("zxcv@098Z");
driver.find_element_by_name("new_password1").clear();
driver.find_element_by_name("new_password1").send_keys("zxcv@098Zz");
driver.find_element_by_name("new_password2").clear();
driver.find_element_by_name("new_password2").send_keys("zxcv@098Zz");
time.sleep(2);
driver.find_element_by_xpath("//input[@value='Change']").click();
time.sleep(2);
try:
    update = driver.find_element_by_xpath("//h1[text()='Password changed']")
    if update.is_displayed():
        update.click();
        print("Password has been successfully changed.")
except NoSuchElementException:
    print("Could not change password")
    print("Test Fail!!!")
    driver.close();
driver.find_element_by_link_text("Logout").click();
time.sleep(2);
driver.close();