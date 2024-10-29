from selenium.webdriver.common.by import By

class HomeLocators:
    logo = (By.CSS_SELECTOR, "#page-header-wrapper > strong > img" )

class failAuth:
    errorMessage = (By.CSS_SELECTOR, "#maincontent > div:nth-child(1) > div > div > div:nth-child(1) > div")
    