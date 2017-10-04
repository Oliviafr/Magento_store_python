#!/usr/bin/python
import unittest
from selenium import webdriver
import os, sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


class MerkeRules(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.EMAIL = "lwilliam670+1004_46@gmail.com"
        # self.PASSWORD = "Ifo10044"
        # self.SEARCH_TEXT_FORGOTPW = "Forgot password?"
        # self.OFACCOUNT = "Olivia Frumin Test Account"

    def test_enroll_with_purchase(self):
        # import pdb
        # pdb.set_trace()
        driver = self.driver
        # self.driver.get("http://magento-stage.500friends.com/furniture")
        self.driver.get("http://magento.500friends.com/furniture")
        time.sleep(2)
        self.driver.get("http://magento.500friends.com/couch.html")
        # driver.find_element_by_link_text("Couch").click()
        # driver.find_element_by_css_selector("body > div > div > div.main.col3-layout > div.col-wrapper > div.col-main > div > div.category-products > ul.products-grid.first.odd > li:nth-child(2) > h2 > a").click()
        time.sleep(3)
        driver.find_element_by_css_selector(
            "#product_addtocart_form > div.product-essential > div.product-shop > div.add-to-box > div > button").click()
        driver.find_element_by_css_selector(
            "body > div > div > div.main.col1-layout > div > div > div.page-title.title-buttons > ul > li > button > span > span").click()
        driver.find_element_by_css_selector("#login" + "\\3a guest").click()
        driver.find_element_by_css_selector("#onepage-guest-register-button > span > span").click()
        driver.find_element_by_css_selector("#billing\\3a firstname").send_keys("Test_FN")
        driver.find_element_by_css_selector("#billing\\3a lastname").send_keys("Test_LN")
        driver.find_element_by_css_selector("#billing\\3a email").send_keys(self.EMAIL)
        driver.find_element_by_css_selector("#billing\\3a street1").send_keys("SF_address")
        driver.find_element_by_css_selector("#billing\\3a city").send_keys("SF")
        select = Select(driver.find_element_by_css_selector("#billing\\3a region_id"))
        driver.find_element_by_css_selector("#billing\\3a postcode").send_keys("654321")
        # print select.options
        # print [o.text for o in select.options]  # these are string-s
        select.select_by_visible_text("California")
        driver.find_element_by_css_selector("#billing\\3a postcode").send_keys("654321")
        driver.find_element_by_css_selector("#billing\\3a telephone").send_keys("0987654321")
        time.sleep(3)
        driver.find_element_by_css_selector("#billing-buttons-container > button > span > span").click()
        time.sleep(4)
        driver.find_element_by_id("s_method_freeshipping_freeshipping").click()
        driver.find_element_by_css_selector("#shipping-method-buttons-container > button > span > span").click()
        time.sleep(5)
        driver.find_element_by_css_selector("#p_method_checkmo").click()
        driver.find_element_by_css_selector("#payment-buttons-container > button > span > span").click()
        time.sleep(5)
        driver.find_element_by_css_selector("#review-buttons-container > button > span > span").click()
        time.sleep(15)

    # def tearDown(self):
    #     self.driver.close()


if __name__ == '__main__':
    unittest.main()
