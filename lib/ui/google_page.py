from lib.base.selenium_driver import SeleniumDriver

class GooglePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def getPageTitle(self):
        return self.pageTitle()
