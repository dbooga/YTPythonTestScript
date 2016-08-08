# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pageobjects


class YTMakePlaylist(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.youtube.com/"
        self.usr_log = "xxxxx@gmail.com"
        self.usr_pass = "xxxxx"
        self.verificationErrors = []
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(self.base_url + "/")
        # Log In with user credentials
        self.homepage = pageobjects.HomePage(self.driver)
        self.homepage.log_in(self.usr_log, self.usr_pass)

    def xtest_account(self):
        """Test account sign in validation"""
        driver = self.driver
        acc_icon = (By.ID, 'yt-masthead-account-picker')
        self.wait.until(EC.visibility_of_element_located(acc_icon))
        icon = driver.find_element(*acc_icon)
        icon.click()
        try: self.assertEqual(self.usr_log, self.homepage.get_email())
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def test_make_playlist(self):
        """Test adding video to new playlist"""
        driver = self.driver
        query = "Python"

        # Search for python videos
        self.homepage.search(query)

        # Select First Python Programming Video
        search_results = pageobjects.SearchResultsPage(driver)
        search_results.select_video()

        # Create new playlist 'pylearn'
        video = pageobjects.VideoPage(driver)
        video.add_to_playlist()

        # Navigate to My Channel page
        video.navigate_channel()

        # Validate 'pylearn' playlist exists
        my_channel = pageobjects.MyChannelPage(driver)
        try: self.assertEqual("pylearn", my_channel.get_playlist())
        except AssertionError as e: self.verificationErrors.append(str(e))

        # Select playlist
        my_channel.select_playlist()

        # Validate 'Python Programming' video is in playlist
        playlist = pageobjects.PlaylistPage(driver)
        try: self.assertEqual("Python Programming", playlist.get_playlist_videos())
        except AssertionError as e: self.verificationErrors.append(str(e))

    def test_delete_playlist(self):
        """Test deleting playlist"""
        driver = self.driver

        # Navigate to My Channel
        self.homepage.navigate_channel()

        # Click pylearn playlist
        my_channel = pageobjects.MyChannelPage(driver)
        my_channel.select_playlist()

        # Delete playlist
        playlist = pageobjects.PlaylistPage(driver)
        playlist.delete_playlist()

    def tearDown(self):
        driver = self.driver
        wait = self.wait
        driver.get(self.base_url + "/")
        # Logout
        self.homepage.log_out()
        # Validate sign out
        sign_in_btn = (By.XPATH, "(//button[@type='button'])[2]")
        wait.until(EC.visibility_of_element_located(sign_in_btn))
        try: self.assertEqual("Sign in", driver.find_element(*sign_in_btn).text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
