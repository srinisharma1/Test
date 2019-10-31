from selenium.webdriver import Chrome, Firefox
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class WebDriverFactory():

    def __init__(self, browser, baseURL):
        self.browser = browser
        self.baseURL = baseURL

    def getWebDriverInstance(self):

        if self.browser == "firefox":
            # Set ie driver
            # driver = Chrome(executable_path='/Users/srinivas/PycharmProjects/Opinion/browsers_exe/chromedriver1')#/Users/srinivas/PycharmProjects/Opinion/browsers_exe/geckodriver
            driver = webdriver.Chrome(ChromeDriverManager().install())

        elif self.browser == "chrome":
            # Set chrome driver
            # driver = Chrome(executable_path='/Users/srinivas/PycharmProjects/Opinion/browsers_exe/chromedriver1')
            driver = webdriver.Chrome(ChromeDriverManager().install())

        else:
            # driver = Chrome(executable_path='/Users/srinivas/PycharmProjects/Opinion/browsers_exe/chromedriver1')
            driver = webdriver.Chrome(ChromeDriverManager().install())

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
