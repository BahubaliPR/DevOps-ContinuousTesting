from selenium import webdriver
import selenium
import unittest
import os
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class WebApp(object):

    def TestApp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driverLocation = "../Drivers/chromedriver"
        baseURL = "http://localhost:80/"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.implicitly_wait(50)

        try:
            driver.maximize_window()
            driver.get(baseURL)
            print("The Browser launched and navigated to URL")

            element = driver.find_element(By.XPATH, ".//body//h1")
            appText = element.text
            print(appText)
            assert appText == 'This is my website'

        except AttributeError:
            print(AttributeError)

        finally:
            driver.close()
            driver.quit()


app = WebApp()
app.TestApp()
