from assertpy import assert_that, soft_assertions
from selenium.webdriver.common.by import By
from locator.locators import HomeLocators, failAuth
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def goToHome(self):
        self.driver.get("https://istyle.ro")
        self.driver.maximize_window()

    def verifyLogo(self):
        logo = self.driver.find_element(*HomeLocators.logo)
        with soft_assertions():
            assert_that(logo).is_true()

    def verifyTitle(self):
        with soft_assertions():
            assert_that(self.driver.title).contains("iSTYLE.ro")

    def reachLogin(self):
        wait = WebDriverWait(self.driver, 10)
        acceptCookies = self.driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        acceptCookies.click()
        authIcon = self.driver.find_element(By.ID, "header-account-toggle")
        authIcon.click()
        loginButton = self.driver.find_element(By.CSS_SELECTOR, "#ui-id-2 > ul > li.authorization-link > a")
        loginButton.click()

    def verifyWrongLogin(self):
        mailField = self.driver.find_element(By.ID, "email").send_keys("asd@asd.com")
        passField = self.driver.find_element(By.ID, "pass").send_keys("anaconda")
        goBtn = self.driver.find_element(By.ID, "send2").click()
        wait = WebDriverWait(self.driver, 10)
        errorMessage = self.driver.find_element(*failAuth.errorMessage)
        with soft_assertions():
            assert_that(errorMessage).is_true()

    def verifyRightLogin(self):
        # iStyle account - hosifof101@regishub.com / Tester123!
        mailField = self.driver.find_element(By.ID, "email").send_keys("hosifof101@regishub.com")
        passField = self.driver.find_element(By.ID, "pass").send_keys("Tester123!")
        loginButton = self.driver.find_element(By.ID, "send2").click()
        wait = WebDriverWait(self.driver, 10)
        with soft_assertions():
            assert_that(self.driver.find_element(By.ID, "header-account-toggle")).is_true()