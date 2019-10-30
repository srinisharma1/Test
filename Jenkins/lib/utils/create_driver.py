from selenium.webdriver import Chrome, Firefox


class WebDriverFactory():

    def __init__(self, browser, baseURL):
        self.browser = browser
        self.baseURL = baseURL

    def getWebDriverInstance(self):

        if self.browser == "firefox":
            # Set ie driver
            driver = Firefox('/Users/srinivas/PycharmProjects/Opinion/browsers_exe/geckodriver')

        elif self.browser == "chrome":
            # Set chrome driver
            driver = Chrome('/Users/srinivas/downloads/chromedriver')
        else:
            driver = Chrome('/Users/srinivas/downloads/chromedriver')

        # SETTING UP THE URL
        if self.baseURL == 'prod':
            # PRODUCTION URL
            baseURL = 'https://www.google.com/'
        elif self.baseURL == 'stg':

            # STAGING URL
            baseURL = 'https://www.google.com/'
        elif self.baseURL == 'dev':

            # DEVELOPMENT URL
            baseURL = 'https://www.google.com/'
        else:

            # DEFAULT URL
            baseURL = 'https://www.google.com/'

        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver
