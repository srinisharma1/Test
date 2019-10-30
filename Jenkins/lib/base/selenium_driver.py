from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import logging
import logging.config
from os import path

class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Clicked on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Cannot click on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            print_stack()

    def pageTitle(self):
        page_title = None
        # page_url = self.pageURL()
        try:
            page_title = self.driver.title
            print("Got the Page title: " + page_title)
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Got the page title: " + page_title)
        except:
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Could not extract the page title: " + page_title)
        return page_title

    def pageURL(self):
        page_url = None
        # page_title = self.pageTitle()
        try:
            page_url = self.driver.current_url
            print("Got the page URL: " + page_url)
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Got the page URL: " + page_url)
        except:
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Could not extract the page title: " + page_url)
        return page_url

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Cannot send data on the element with locator: " + locator +
                  " locatorType: " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
                logging.config.fileConfig(log_file_path)
                logger = logging.getLogger()
                logger.info("Element Found")
                return True
            else:
                log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
                logging.config.fileConfig(log_file_path)
                logger = logging.getLogger()
                logger.info("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, byType):
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
                logging.config.fileConfig(log_file_path)
                logger = logging.getLogger()
                logger.info("Element Found")
                return True
            else:
                log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
                logging.config.fileConfig(log_file_path)
                logger = logging.getLogger()
                logger.info("Element not found")
                return False
        except:
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5,typeofwait="visibility_of"):
        element = None
        try:
            byType = self.getByType(locatorType)
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of((byType,locator)))
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Element appeared on the web page")
        except:
            log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
            logging.config.fileConfig(log_file_path)
            logger = logging.getLogger()
            logger.info("Element not appeared on the web page")
            print_stack()
        return element

    '''
        def waitForElement(self, locator, locatorType="id",
                               timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            logger.info("Waiting for maximum :: " + str(timeout) +
                  " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            logger.info("Element appeared on the web page")
        except:
            logger.info("Element not appeared on the web page")q
            print_stack()
        return element
    '''
