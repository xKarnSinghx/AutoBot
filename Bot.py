from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def create_account(url):
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(
            EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='reCAPTCHA']"))
        )

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "recaptcha-anchor"))
        ).click()

        driver.switch_to.default_content()

    except (TimeoutException, NoSuchElementException):
        print("Could not solve the reCAPTCHA. Manual intervention is required.")


for i in range(1, 2):
    URL = 'https://www.google.com/recaptcha/api2/demo'
    create_account(URL)
    print(f"Account {i} is made")
