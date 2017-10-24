# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

#
# SE DEBE CORRER CON PYTHON 2.7 Y FIREFOX 54.0
#

class Seleniumtests(unittest.TestCase):
    def setUp(self):
       
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_seleniumtests(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("Create carousel(current)").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("nuevoc")
        driver.find_element_by_id("id_count").clear()
        driver.find_element_by_id("id_count").send_keys("2")
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("cont1")
        driver.find_element_by_id("id_description").clear()
        driver.find_element_by_id("id_description").send_keys("desc1")
        driver.find_element_by_id("id_url").clear()
        driver.find_element_by_id("id_url").send_keys("1")
        driver.find_element_by_id("id_image").clear()
        driver.find_element_by_id("id_image").send_keys("/home/roberto/git/Django_Carrusel/carrusel/static/images/tree1.jpg")
        driver.find_element_by_id("id_1-title").clear()
        driver.find_element_by_id("id_1-title").send_keys("cont2")
        driver.find_element_by_id("id_1-description").clear()
        driver.find_element_by_id("id_1-description").send_keys("desc2")
        driver.find_element_by_id("id_1-url").clear()
        driver.find_element_by_id("id_1-url").send_keys("2")
        driver.find_element_by_id("id_1-image").clear()
        driver.find_element_by_id("id_1-image").send_keys("/home/roberto/git/Django_Carrusel/carrusel/static/images/tree2.jpeg")
        driver.find_element_by_css_selector("button.btn.btn-default").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
