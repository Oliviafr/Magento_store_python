#!/usr/bin/python
import unittest
from selenium import webdriver
import os, sys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class MerkeRules (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.USERNAME = "ofrumin@live.com"
        self.PASSWORD = "Ifo10044"
        self.SEARCH_TEXT_FORGOTPW = "Forgot password?"
        self.OFACCOUNT = "Olivia Frumin Test Account"
    def test_first_rulesdefinition(self):
        # import pdb
        # pdb.set_trace()
        driver = self.driver
        self.driver.get("https://loyalty-stage.500friends.com/login")
        driver.find_element(By.XPATH, "//input[@id='user_session_email']").click()
        driver.find_element(By.XPATH, "//input[@id='user_session_email']").send_keys(self.USERNAME)

        for x in self.driver.find_elements_by_xpath(".//*[@class='password clear']"):
            link = webdriver.ActionChains(self.driver).move_to_element(x).click(x).perform()
        for x in self.driver.find_elements_by_xpath(".//*[@class='password clear']"):
            link = webdriver.ActionChains(self.driver).move_to_element(x).send_keys(self.PASSWORD).perform()
        forgotPW = driver.find_element_by_link_text('Forgot password?').text
        self.assertIn(self.SEARCH_TEXT_FORGOTPW, forgotPW)
        driver.implicitly_wait(2000)
        driver.find_element_by_id("sign_in").click()
        accountHeader  = driver.find_element_by_css_selector("div.primary_wrap h1").text
        assert accountHeader == self.OFACCOUNT, "Houston we've got a problem"
        self.driver.get("https://loyalty-stage.500friends.com/accounts/415/rules/new")
        driver.find_element_by_id("point_rule_event_type").send_keys("Promotion")
        driver.find_element_by_id("point_rule_description").send_keys("Description")
        driver.find_element_by_id("point_rule_display_detail").send_keys("Details")

        # Uplouding photo
        Imagepath = os.path.abspath('C:\Users\ofrum\Desktop\self_img.pneg')
        print Imagepath.format()
        # driver.find_element_by_link_text("Upload a picture").click()
        # driver.find_element_by_class_name("image_url").send_keys(Imagepath)

        imgbox = driver.find_element_by_class_name("image_url").is_displayed()
        print imgbox
        driver.find_element_by_css_selector("#point_rule_display_icon_url > div.image_upload > div > div > span").send_keys(Imagepath)


        # JavascriptExecutor js = (JavascriptExecutor) driver;
        # js.executeScript("arguments[0].setAttribute('style', arguments[1])",` driver.findElement(By.xpath("//input[@type='file']")), "0");
        # js.executeScript("arguments[0].setAttribute('class', arguments[1])", driver.findElement(By.xpath("//input[@type='file']/../../div[2]")), "a");
        # driver.findElement(By.xpath("//input[@type='file']")).sendKeys("Your Path to the file your system");

        # driver.find_element_by_link_text("Upload a picture").send_keys(Imagepath)
        # driver.find_element_by_css_selector(self.CONFIRM_PHOTO_CLASS).click()


        # driver.find_element_by_id("point_rule_value_fixed").send_keys("700")
        # select = Select(driver.find_element_by_id("point_rule_limit_selection"))
        # print select.options
        # print [o.text for o in select.options]  # these are string-s
        # select.select_by_visible_text("Limit Points")
        # driver.find_element_by_id("points_limit").clear()
        # driver.find_element_by_id("points_limit").send_keys("100")
        # driver.find_element_by_id("manual").click()
        # pointsmanually =  driver.find_element_by_xpath(".//*[@id='timeframe_manual']/dt")
        # assert pointsmanually.text == "Points will be manually approved by you.", "Houston we've got a problem"
        #
        # driver.find_element_by_id("point_rule_destination_url").send_keys("https://loyalty-stage.500friends.com/login")
        # driver.find_element_by_id("point_rule_active").click()
        # driver.find_element_by_link_text("Cancel").click()
        #
        # accountHeader  = driver.find_element_by_css_selector("div.primary_wrap h1").text
        # assert accountHeader == self.OFACCOUNT, "Houston we've got a problem"
        # def tearDown(self):
        #     self.driver.close()

if __name__ == '__main__':
    unittest.main()
