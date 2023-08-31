from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def create_account(url, email, password):
    driver = webdriver.Firefox()
    driver.get(url)

    login_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='MuiButton-label' and contains(text(), 'Login')]"))
    )
    login_btn.click()

    signup_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[@class='MuiTab-wrapper' and contains(text(), 'Sign Up')]"))
    )
    signup_btn.click()

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[contains(text(), 'Enter Email')]/following-sibling::div/input"))
    )
    email_input.send_keys(email)

    password_input = driver.find_element(By.XPATH,
                                         "//label[contains(text(), 'Enter Password')]/following-sibling::div/input")
    password_input.send_keys(password)

    confirm_password_input = driver.find_element(By.XPATH,
                                                 "//label[contains(text(), 'Confirm "
                                                 "Password')]/following-sibling::div/input")
    confirm_password_input.send_keys(password)
    try:
        signup_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button/span[@class='MuiButton-label' and text()='Sign Up']"))
        )
        signup_button.click()

    except (TimeoutException, NoSuchElementException):
        print("Unsuccessfull SignUp with %s and %s " % (TimeoutException, NoSuchElementException))

    try:
        signup_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(@class, 'MuiButton-root') and .//span[text()='Sign Up']]"))
        )
        signup_button.click()

    except (TimeoutException, NoSuchElementException):
        print("Unsuccessfull SignUp with %s and %s " % (TimeoutException, NoSuchElementException))

    try:
        button = driver.find_element(By.XPATH,
                                     "//button[contains(@class, 'MuiButton-root') and .//span[text()='Sign Up']]")
        driver.execute_script("arguments[0].click();", button)

    except (TimeoutException, NoSuchElementException):
        print("Unsuccessfull SignUp with %s and %s " % (TimeoutException, NoSuchElementException))

    success_message_xpath = f"//*[contains(text(), 'Sign Up Successful. Welcome {email}')]"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, success_message_xpath))
    )

    driver.quit()


for i in range(1, 10):
    URL = 'https://crypto-hunter.netlify.app/'
    EMAIL = f'test00{i}_email@example.com'
    PASSWORD = 'test_password123'

    create_account(URL, EMAIL, PASSWORD)
    print(f"Account {i} is made")
