import time
from selenium import webdriver
import requests
from faker import Faker
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import random
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

fake = Faker()





class ChromeBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()


    def test_QuoteForm_positive(self):
        driver = self.driver

        # Check that an element is present on the DOM of a page and visible.
        url = "https://qatest.datasub.com/"
        driver.get(url)
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # driver sleep from 1 to 5 seconds
        def delay():
            time.sleep(random.randint(1, 5))

        # Check current webpage Title with Exception functionality
        try:
            assert "Startup - Home" in driver.title
        except WDE:
            print("Webpage is different, current Title is: ", driver.title)

        delay()

        # API testing from Selenium
        print("Webpage Url has", requests.get(url).status_code, "as status Code")
        code = requests.get(url).status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        # Check that an element is present_ Quote element on the navigation bar
        try:
            driver.find_element(By.XPATH, '//*[@class="nav-item nav-link"]  [@href="quote.html"]').click()
        except WDE:
            print("Quote element on the navigation bar is missing or not clickable")

        delay()

        # Check Quote Form on the page
        QF = driver.find_element(By.XPATH, "//button[contains(text(),'Request A Quote')]")
        ActionChains(driver).scroll_to_element(QF).perform()
        try:
            if QF:
                driver.get_screenshot_as_file("QForm from Quote link_Chrome.png")
        except WDE:
            print("Quote Form from tne link of the navigation bar is missing")

        driver.back()
        delay()

        # Check that an element is present_ Quote FreeQuote button
        try:
            driver.find_element(By.LINK_TEXT, "Free Quote").click()
        except WDE:
            print("FreeQuote button is missing")
        delay()

        # Check Quote Form on the page
        QF = driver.find_element(By.XPATH, "//button[contains(text(),'Request A Quote')]")
        ActionChains(driver).scroll_to_element(QF).perform()
        try:
            if QF:
                driver.get_screenshot_as_file("QForm from Quote button_Chrome.png")
        except WDE:
            print("Quote Form from FreeQuote button is missing")

        driver.back()
        delay()

        QF = driver.find_element(By.XPATH, "//button[contains(text(),'Request A Quote')]")
        ActionChains(driver).scroll_to_element(QF).perform()

        delay()

        # Print out the Quote Form
        driver.get_screenshot_as_file("QForm from scroll_Chrome.png")

        # Check Quote Form on the page
        try:
            driver.find_element(By.ID, "subscriptionForm").is_displayed()
        except WDE:
            print("Quote Form is missing")


        # filling out the form, Your Name
        driver.find_element(By.ID, "name").send_keys(fake.first_name())

        # filling out the form, Your Email
        driver.find_element(By.ID, "email").send_keys(fake.email())

        # filling out the form, Click Terms checkbox
        Select(driver.find_element(By.XPATH, "//select[@id='service']")).select_by_visible_text("Select B Service")

        # filling out the form, Message
        driver.find_element(By.XPATH, "//textarea[contains(@id,'message')]").send_keys("Hello,World!")

        # filling out the form, Click Continue button
        driver.find_element(By.XPATH, "//button[contains(text(),'Request A Quote')]").click()



        delay()


    def test_QuoteForm_negative(self):
        driver = self.driver

        # Check that an element is present on the DOM of a page and visible.
        url = "https://qatest.datasub.com/"
        driver.get(url)
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # driver sleep from 1 to 5 seconds
        def delay():
            time.sleep(random.randint(1, 5))

        # Check current webpage Title with Exception functionality
        try:
            assert "Startup - Home" in driver.title
        except WDE:
            print("Webpage is different, current Title is: ", driver.title)

        delay()


        QF = driver.find_element(By.XPATH, "//button[contains(text(),'Request A Quote')]")
        ActionChains(driver).scroll_to_element(QF).perform()

        delay()


        # Check Quote Form on the page
        try:
            driver.find_element(By.ID, "subscriptionForm").is_displayed()
        except WDE:
            print("Quote Form is missing")

        # filling out the form
        try:
            driver.find_element(By.ID, "name").send_keys('1%!= ""')
            print("Quote Form accepts invalid characters in field Name")
            driver.find_element(By.ID, "email").send_keys(".abc@mail.com")
            print("Quote Form accepts invalid email")
            Select(driver.find_element(By.XPATH, "//select[@id='service']")).select_by_visible_text("Select B Service")
            driver.find_element(By.XPATH, "//textarea[contains(@id,'message')]").send_keys("Hello,World!")
            driver.find_element(By.XPATH, "//button[contains(text(),'Request A Quote')]").click()
        except WDE:
            print("Quote Form does not accept invalid characters")

        delay()


    def tearDown(self):
        self.driver.quit()




class EdgeBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()


    def test_QuoteForm_positive(self):
        driver = self.driver

        # Check that an element is present on the DOM of a page and visible.
        url = "https://qatest.datasub.com/"
        driver.get(url)
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # driver sleep from 1 to 5 seconds
        def delay():
            time.sleep(random.randint(1, 5))

        # Check current webpage Title with Exception functionality
        try:
            assert "Startup - Home" in driver.title
        except WDE:
            print("Webpage is different, current Title is: ", driver.title)

        delay()

        # API testing from Selenium
        print("Webpage Url has", requests.get(url).status_code, "as status Code")
        code = requests.get(url).status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        # Check that an element is present_ Quote element on the navigation bar
        try:
            driver.find_element(By.XPATH, '//*[@class="nav-item nav-link"]  [@href="quote.html"]').click()
        except WDE:
            print("Quote element on the navigation bar is missing or not clickable")

        delay()

        # Check Quote Form on the page
        QF = driver.find_element(By.XPATH, "//button[contains(text(),'Request A Quote')]")
        ActionChains(driver).scroll_to_element(QF).perform()
        try:
            if QF:
                driver.get_screenshot_as_file("QForm from Quote link_EDGE.png")
        except WDE:
            print("Quote Form from tne link of the navigation bar is missing")

        driver.back()
        delay()

        # Check that an element is present_ Quote FreeQuote button
        try:
            driver.find_element(By.LINK_TEXT, "Free Quote").click()
        except WDE:
            print("FreeQuote button is missing")
        delay()

        # Check Quote Form on the page
        QF = driver.find_element(By.XPATH, "//button[contains(text(),'Request A Quote')]")
        ActionChains(driver).scroll_to_element(QF).perform()
        try:
            if QF:
                driver.get_screenshot_as_file("QForm from Quote button_EDGE.png")
        except WDE:
            print("Quote Form from FreeQuote button is missing")

        driver.back()
        delay()

        QF = driver.find_element(By.XPATH, "//button[contains(text(),'Request A Quote')]")
        ActionChains(driver).scroll_to_element(QF).perform()

        delay()

        # Print out the Quote Form
        driver.get_screenshot_as_file("QForm from scroll_EDGE.png")

        # Check Quote Form on the page
        try:
            driver.find_element(By.ID, "subscriptionForm").is_displayed()
        except WDE:
            print("Quote Form is missing")


        # filling out the form, Your Name
        driver.find_element(By.ID, "name").send_keys(fake.first_name())

        # filling out the form, Your Email
        driver.find_element(By.ID, "email").send_keys(fake.email())

        # filling out the form, Click Terms checkbox
        Select(driver.find_element(By.XPATH, "//select[@id='service']")).select_by_visible_text("Select B Service")

        # filling out the form, Message
        driver.find_element(By.XPATH, "//textarea[contains(@id,'message')]").send_keys("Hello,World!")

        # filling out the form, Click Continue button
        driver.find_element(By.XPATH, "//button[contains(text(),'Request A Quote')]").click()



        delay()


    def test_QuoteForm_negative(self):
        driver = self.driver

        # Check that an element is present on the DOM of a page and visible.
        url = "https://qatest.datasub.com/"
        driver.get(url)
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # driver sleep from 1 to 5 seconds
        def delay():
            time.sleep(random.randint(1, 5))

        # Check current webpage Title with Exception functionality
        try:
            assert "Startup - Home" in driver.title
        except WDE:
            print("Webpage is different, current Title is: ", driver.title)

        delay()


        QF = driver.find_element(By.XPATH, "//button[contains(text(),'Request A Quote')]")
        ActionChains(driver).scroll_to_element(QF).perform()

        delay()


        # Check Quote Form on the page
        try:
            driver.find_element(By.ID, "subscriptionForm").is_displayed()
        except WDE:
            print("Quote Form is missing")

        # filling out the form
        try:
            driver.find_element(By.ID, "name").send_keys('1%!= ""')
            print("Quote Form accepts invalid characters in field Name")
            driver.find_element(By.ID, "email").send_keys(".abc@mail.com")
            print("Quote Form accepts invalid email")
            Select(driver.find_element(By.XPATH, "//select[@id='service']")).select_by_visible_text("Select B Service")
            driver.find_element(By.XPATH, "//textarea[contains(@id,'message')]").send_keys("Hello,World!")
            driver.find_element(By.XPATH, "//button[contains(text(),'Request A Quote')]").click()
        except WDE:
            print("Quote Form does not accept invalid characters")

        delay()


    def tearDown(self):
        self.driver.quit()








if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))