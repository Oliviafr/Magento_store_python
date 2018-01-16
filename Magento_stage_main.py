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
        self.EMAIL = "lwilliam670+0116_3.0@gmail.com"
        # self.PASSWORD = "Ifo10044"
        # self.SEARCH_TEXT_FORGOTPW = "Forgot password?"
        # self.OFACCOUNT = "Olivia Frumin Test Account"

    def test_enroll_with_purchase(self):
        # import pdb
        # pdb.set_trace()
        driver = self.driver
        self.driver.get("http://magento-stage.500friends.com/furniture")
        time.sleep(4)
        driver.find_element_by_css_selector(
            "body > div > div > div.main.col3-layout > div.col-wrapper > div.col-main > div > div.category-products > ul.products-grid.first.odd > li:nth-child(2) > div.actions > button").click()
        driver.find_element_by_css_selector(
            "body > div > div > div.main.col1-layout > div > div > div.page-title.title-buttons > ul > li > button > span > span").click()
        time.sleep(4)
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
        time.sleep(4)
        driver.find_element_by_id("billing:fax").click()
        time.sleep(2)
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
        # driver.find_element_by_css_selector("#billing-buttons-container > button > span > span").click()
        # time.sleep(5)
        # driver.find_element_by_css_selector("#s_method_freeshipping_freeshipping").click()
        # driver.find_element_by_css_selector("#shipping-method-buttons-container > button > span > span").click()
        # time.sleep(5)
        # driver.find_element_by_css_selector("#p_method_checkmo").click()
        # driver.find_element_by_css_selector("#payment-buttons-container > button > span > span").click()
        # time.sleep(5)
        # driver.find_element_by_css_selector("#review-buttons-container > button > span > span").click()
        # time.sleep(15)

        # HTTPS - LP
        #-----------------------------------------------------------------------------
        #-----------------------------------------------------------------------------
        # driver.switchTo().activeElement()
        # driver.switchTo().frame("easyXDM__ffLoyalty__ffxd_provider")

        # driver.find_element_by_css_selector("#new > div.focus > table > tbody > tr:nth-child(2) > td > div:nth-child(2) > a").click()
        # driver.find_element_by_css_selector("#new > div.focus > div.focus > table > tbody > tr:nth-child(3) > td > div.blue_button_wrapper > a").click()
        # driver.find_element_by_css_selector("#height_wrapper > div.facebook_share_widget.off_state > div.content_wrap.facebook.social_share > ul > li.social_share_facebook.selected > div.network_button").click()
        # driver.find_element_by_css_selector("#share_message").send_keys("blablabla")
        # driver.find_element_by_css_selector("#facebook_share_form > div.bottom_wrap.clear > ul > li > input").click()
        # # self.driver.get(
        #     "https://loyalty-stage.500friends.com/thankyou_widget/new?auto_resize=true&container_id=ffLoyaltyWidget_TVSVE&cross_domain=true&email="+self.EMAIL+"&event_id="+"100002534"+"&panel=welcome&referral_tracking=true&url=http%3A%2F%2Fmagento-stage.500friends.com%2Fcheckout%2Fonepage%2Fsuccess%2F&uuid=&value=649.49&wid=ujM2wMCr2m#")
        # driver.find_element_by_css_selector("#new > div.focus > table > tbody > tr:nth-child(2) > td > div:nth-child(2) > a").click()
        # driver.find_element_by_css_selector("#new > div.focus > div.focus > table > tbody > tr:nth-child(3) > td > div.blue_button_wrapper > a").click()
        #
        # self.assertIn(self.SEARCH_TEXT_FORGOTPW, forgotPW)




    # def tearDown(self):
    #     self.driver.close()


if __name__ == '__main__':
    unittest.main()

