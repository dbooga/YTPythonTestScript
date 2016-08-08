from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    # GO_BUTTON = (By.ID, 'submit')

    sign_in_btn = (By.XPATH, "(//button[@type='button'])[2]")

    # (By.XPATH, "//a[contains(text(),'pylearn')]")

class SignInPageLocators(object):
    email = (By.ID, "Email")
    next_btn = (By.ID, "next")
    password = (By.ID, "Passwd")
    sign_in = (By.ID, "signIn")
"""
    driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
    driver.find_element_by_id("Email").clear()
    driver.find_element_by_id("Email").send_keys("dooone321@gmail.com")
    driver.find_element_by_id("next").click()
    wait.until(EC.visibility_of_element_located((By.ID, 'Passwd')))
    driver.find_element_by_id("Passwd").clear()
    driver.find_element_by_id("Passwd").send_keys("doone123")
    driver.find_element_by_id("signIn").click()
"""
class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass