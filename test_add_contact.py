# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://localhost/addressbook/index.php")
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_id("LoginForm").submit()
        driver.find_element_by_link_text("add new").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(u"Юзер")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(u"Тестовый")
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(u"ООО \"Рога и копыта\"")
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(u"Москва, Кремль")
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("111111111")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("22222222")
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("test@yopmail.com")
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("6")
        driver.find_element_by_xpath("//option[@value='6']").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("February")
        driver.find_element_by_xpath("//option[@value='February']").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1987")
        driver.find_element_by_name("new_group").click()
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
