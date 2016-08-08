# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.support.wait import WebDriverWait


class YTdeletePlaylist(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.youtube.com/"
        self.verificationErrors = []
        self.wait = WebDriverWait(self.driver, 10)

    def test_make_playlist(self):
        driver = self.driver
        wait = self.wait
        driver.get(self.base_url + "/")

        # Signing in
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_id("Email").clear()
        driver.find_element_by_id("Email").send_keys("dooone321@gmail.com")
        driver.find_element_by_id("next").click()
        wait.until(EC.visibility_of_element_located((By.ID, 'Passwd')))
        driver.find_element_by_id("Passwd").clear()
        driver.find_element_by_id("Passwd").send_keys("doone123")
        driver.find_element_by_id("signIn").click()

        # Validating Account login
        wait.until(EC.visibility_of_element_located((By.ID, 'yt-masthead-account-picker')))
        driver.find_element_by_id("yt-masthead-account-picker").click()
        try:
            self.assertEqual("dooone321@gmail.com", driver.find_element_by_link_text("dooone321@gmail.com").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        # Navigate to My Channel
        driver.find_element_by_xpath("//li[@id='UCWjLO6oQ1a0Idp_LQsUJWAg-guide-item']/a/span/span[2]/span").click()

        # Wait for playlists to populate
        wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'pylearn')]")))

        # Click pylearn playlist
        driver.find_element_by_xpath("//a[contains(text(),'pylearn')]").click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='pl-header']/div[2]/div/div/div/div/h1")))

        # Delete playlist
        driver.find_element_by_xpath("(//button[@type='button'])[32]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[53]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[36]").click()

        # Wait for delete process to complete
        time.sleep(5)

        # Logout
        wait.until(EC.visibility_of_element_located((By.ID, "yt-masthead-account-picker")))
        driver.find_element_by_css_selector("button.yt-masthead-user-icon").click()
        driver.find_element_by_css_selector("a[href='/logout']").click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "(//button[@type='button'])[2]")))
        self.assertEqual("Sign in", driver.find_element_by_xpath("(//button[@type='button'])[2]").text)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
