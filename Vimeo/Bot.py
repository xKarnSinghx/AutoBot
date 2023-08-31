from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def create_account(url, email, password, name):
    driver = webdriver.Firefox()
    driver.get(url)

    try:
        join_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,
                                        "//button[contains(@class, 'sc-1ln0sw6-0 cmMSFw sc-1ekvrxa-18 hvsMAJ') and "
                                        "contains(text(),'Join')]"))
        )
        join_button.click()

    except (TimeoutException, NoSuchElementException):
        print("Unsuccessful Join with %s and %s " % (TimeoutException, NoSuchElementException))

    try:
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='name']"))
        )
        name_input.send_keys(name)

    except (TimeoutException, NoSuchElementException):
        print("Invalid Entry with %s and %s " % (TimeoutException, NoSuchElementException))

    try:
        new_email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='login_email']"))
        )
        new_email_input.send_keys(email)
    except (TimeoutException, NoSuchElementException):
        print("Invalid Entry with %s and %s " % (TimeoutException, NoSuchElementException))

    try:
        new_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
        )
        new_password_input.send_keys(password)
    except (TimeoutException, NoSuchElementException):
        print("Invalid Entry with %s and %s " % (TimeoutException, NoSuchElementException))

    try:
        join_email_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'sc-rn68h5-2') and contains(text(), 'Join with email')]"))
        )

        join_email_btn.click()
    except (TimeoutException, NoSuchElementException):
        print("Invalid credentials with %s and %s " % (TimeoutException, NoSuchElementException))

    try:
        skip_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'sc-jrQzAO') and contains(text(), 'Skip')]"))
        )
        skip_btn.click()
    except (TimeoutException, NoSuchElementException):
        print("Invalid Click with %s and %s " % (TimeoutException, NoSuchElementException))

    driver.quit()


for i in range(1, 10):
    URL = 'https://vimeo.com'
    EMAIL = f'testx00{i}_email@example.com'
    PASSWORD = 'testX_password123'
    NAME = f'test{i}xyssys'

    create_account(URL, EMAIL, PASSWORD, NAME)
    print(f"Account {i} is made")
