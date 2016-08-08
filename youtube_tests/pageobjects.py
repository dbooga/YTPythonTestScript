from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


class HomePage(BasePage):
    SIGN_IN_BTN = (By.XPATH, "(//button[@type='button'])[2]")
    EMAIL = (By.ID, "Email")
    NEXT_BTN = (By.ID, "next")
    PASSWORD = (By.ID, "Passwd")
    SIGN_IN = (By.ID, "signIn")
    ICON = (By.ID, "yt-masthead-account-picker")
    ICON_BTN = (By.CSS_SELECTOR, "button.yt-masthead-user-icon")
    LOGOUT_BTN = (By.CSS_SELECTOR, "a[href='/logout']")
    SEARCH_INPUT = (By.ID, "masthead-search-term")
    SEARCH_BTN = (By.ID, "search-btn")
    ACC = (By.LINK_TEXT, "dooone321@gmail.com")
    MY_CHANNEL = (By.XPATH, "//li[@id='UCWjLO6oQ1a0Idp_LQsUJWAg-guide-item']/a/span/span[2]/span")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_email(self):
        return self.driver.find_element(*self.ACC).text

    def log_in(self, usr_log, usr_pass):
        wait = self.wait
        driver = self.driver
        sign_in_btn = driver.find_element(*self.SIGN_IN_BTN)
        sign_in_btn.click()
        email = driver.find_element(*self.EMAIL)
        email.click()
        email.clear()
        email.send_keys(usr_log)
        next = driver.find_element(*self.NEXT_BTN)
        next.click()
        wait.until(EC.visibility_of_element_located(self.PASSWORD))
        password = driver.find_element(*self.PASSWORD)
        password.clear()
        password.send_keys(usr_pass)
        signin = driver.find_element(*self.SIGN_IN)
        signin.click()

    def log_out(self):
        driver = self.driver
        wait = self.wait

        time.sleep(5)
        wait.until(EC.visibility_of_element_located(self.ICON))
        icon_btn = driver.find_element(*self.ICON_BTN)
        icon_btn.click()
        logout = driver.find_element(*self.LOGOUT_BTN)
        logout.click()

    def search(self, query):
        # Search python videos
        search = self.driver.find_element(*self.SEARCH_INPUT)
        search.clear()
        search.send_keys(query)
        search_btn = self.driver.find_element(*self.SEARCH_BTN)
        search_btn.click()

    def navigate_channel(self):
        my_channel = self.driver.find_element(*self.MY_CHANNEL)
        my_channel.click()


class SearchResultsPage(BasePage):
    VIDEO = (By.CSS_SELECTOR, "a[title='Python Programming'")

    def __init__(self, driver):
        self.driver = driver

    def select_video(self):
        time.sleep(3)
        video = self.driver.find_element(*self.VIDEO)
        video.click()


class VideoPage(BasePage):
    PLAYLIST_NAME = "pylearn"
    VIDEO = (By.CSS_SELECTOR, "a[title='Python Programming'")
    LOAD_TRAY = (By.ID, 'watch8-secondary-actions')
    ADD_TO = (By.CSS_SELECTOR, "button[title='Add to']")
    CREATE_PLAYLIST = (By.CSS_SELECTOR, 'button.create-playlist-item')
    PLAYLIST_ENTRY = (By.XPATH, "(//input[@name='n'])[2]")
    SUBMIT_PLAYLIST_BTN = (By.XPATH, "(//button[@type='submit'])[3]")
    GUIDE_BTN = (By.ID, "appbar-guide-button")
    MY_CHANNEL = (By.XPATH, "//li[@id='UCWjLO6oQ1a0Idp_LQsUJWAg-guide-item']/a/span/span[2]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_to_playlist(self):
        wait = self.wait
        driver = self.driver

        # Create new playlist 'pylearn'
        wait.until(EC.visibility_of_element_located(self.LOAD_TRAY))
        add_to_btn = driver.find_element(*self.ADD_TO)
        add_to_btn.click()
        wait.until(EC.visibility_of_element_located(self.CREATE_PLAYLIST))
        create_playlist = driver.find_element(*self.CREATE_PLAYLIST)
        # swapped from click() to bypass selector wrapped in div/span
        create_playlist.send_keys(Keys.ENTER)
        playlist_entry = driver.find_element(*self.PLAYLIST_ENTRY)
        playlist_entry.clear()
        playlist_entry.send_keys(self.PLAYLIST_NAME)
        playlist_entry.send_keys(Keys.ENTER)
        submit_playlist_btn = driver.find_element(*self.SUBMIT_PLAYLIST_BTN)
        submit_playlist_btn.click()

    def navigate_channel(self):
        self.driver.find_element(*self.GUIDE_BTN).click()
        my_channel = self.driver.find_element(*self.MY_CHANNEL)
        my_channel.click()


class MyChannelPage(BasePage):
    PLAYLIST = (By.XPATH, "//a[contains(text(),'pylearn')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_playlist(self):
        self.wait.until(EC.visibility_of_element_located(self.PLAYLIST))
        return self.driver.find_element(*self.PLAYLIST).text

    def select_playlist(self):
        self.wait.until(EC.visibility_of_element_located(self.PLAYLIST))
        playlist = self.driver.find_element(*self.PLAYLIST)
        playlist.click()


class PlaylistPage(BasePage):
    PLAYLIST_NAME = (By.LINK_TEXT, "Python Programming")
    LOAD_IN = (By.XPATH, "//div[@id='pl-header']/div[2]/div/div/div/div/h1")
    CONTEXT_MENU = (By.XPATH, "(//button[@type='button'])[32]")
    DELETE_BTN = (By.XPATH, "(//button[@type='button'])[53]")
    CONFIRM_BTN = (By.XPATH, "(//button[@type='button'])[36]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_playlist_videos(self):
        self.wait.until(EC.visibility_of_element_located(self.PLAYLIST_NAME))
        return self.driver.find_element(*self.PLAYLIST_NAME).text

    def delete_playlist(self):
        driver = self.driver
        self.wait.until(EC.visibility_of_element_located(self.LOAD_IN))
        # Delete playlist
        driver.find_element(*self.CONTEXT_MENU).click()
        driver.find_element(*self.DELETE_BTN).click()
        driver.find_element(*self.CONFIRM_BTN).click()
        # Wait for delete process to complete
        time.sleep(3)
