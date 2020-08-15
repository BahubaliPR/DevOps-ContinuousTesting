from selenium import webdriver
import os
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class WebApp(object):

    def TestApp(self):
        driverLocation = "../Drivers/chromedriver.exe"
        baseURL = "https://letskodeit.teachable.com/p/practice"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.implicitly_wait(50)

        try:
            driver.maximize_window()
            driver.get(baseURL)
            print("The Browser launched and navigated to URL")

        except AttributeError:
            print(AttributeError)

        finally:
            driver.close()
            driver.quit()


app = WebApp()
app.TestApp()
