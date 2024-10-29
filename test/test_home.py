from selenium import webdriver
import path_config
from page.home_page import HomePage as HP
import unittest
import sys
print(sys.path)

class navTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_logo(self):
        homePage = HP(self.driver)
        homePage.goToHome()
        homePage.verifyLogo()

    def test_title(self):
        homePage = HP(self.driver)
        homePage.goToHome()
        homePage.verifyTitle()

    def test_authBtn(self):
        homePage = HP(self.driver)
        homePage.goToHome()
        homePage.reachLogin()

    def test_wrongLogin(self):
        homePage = HP(self.driver)
        homePage.goToHome()
        homePage.reachLogin()
        homePage.verifyWrongLogin()

    def test_rightLogin(self):
        homePage = HP(self.driver)
        homePage.goToHome()
        homePage.reachLogin()
        homePage.verifyRightLogin() 

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()