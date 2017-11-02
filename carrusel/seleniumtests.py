# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Selenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://127.0.0.1:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_selenium(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_link_text("NineSoft").click()
        driver.find_element_by_link_text("Crear Breadcrumbs").click()
        driver.find_element_by_link_text("LINK1").click()
        driver.find_element_by_link_text("interno 1").click()
        time.sleep(1)
        driver.find_element_by_link_text("interno 2").click()
        driver.find_element_by_link_text("interno 3").click()
        time.sleep(1)
        driver.find_element_by_link_text("Link 1").click()
        driver.find_element_by_link_text("Home").click()
        time.sleep(1)
        driver.find_element_by_link_text("LINK2").click()
        driver.find_element_by_link_text("Home").click()
        time.sleep(1)
        driver.find_element_by_link_text("LINK3").click()
        driver.find_element_by_link_text("Home").click()
        
        time.sleep(1)
        
        driver.find_element_by_link_text(u"Crear Paginación").click()
        driver.find_element_by_id("newElem").clear()
        driver.find_element_by_id("newElem").send_keys("elementonuevo")
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(1)
        driver.find_element_by_id("numberOfElements").clear()
        driver.find_element_by_id("numberOfElements").send_keys("1")
        time.sleep(1)
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        driver.find_element_by_link_text(u"»").click()
        driver.find_element_by_link_text(u"»").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"«").click()
        driver.find_element_by_link_text(u"«").click()
        
        time.sleep(1)
        
        driver.find_element_by_link_text("Crear Carrusel(current)").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("carrusel")
        driver.find_element_by_id("id_count").clear()
        driver.find_element_by_id("id_count").send_keys("2")
        time.sleep(1)
        driver.find_element_by_css_selector("button.btn.btn-secondary").click()
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys("uno")
        time.sleep(1)
        driver.find_element_by_id("id_description").clear()
        driver.find_element_by_id("id_description").send_keys("desc1")
        driver.find_element_by_id("id_image").clear()
        driver.find_element_by_id("id_image").send_keys("/home/roberto/git/Django_Patrones/carrusel/static/images/tree1.jpg")
        driver.find_element_by_id("id_1-title").clear()
        driver.find_element_by_id("id_1-title").send_keys("dos")
        driver.find_element_by_id("id_1-description").clear()
        driver.find_element_by_id("id_1-description").send_keys("desc2")
        time.sleep(1)
        driver.find_element_by_id("id_1-image").clear()
        driver.find_element_by_id("id_1-image").send_keys("/home/roberto/git/Django_Patrones/carrusel/static/images/tree3.jpeg")
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        driver.find_element_by_xpath("//div[2]/i").click()
    
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