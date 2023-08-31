import selenium
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

    # Locate iframe by any attribute (like class, id, etc.)
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
    )
    # switch to the reCaptcha iframe
    # First, switch back to the default content
    driver.switch_to.default_content()

    # Find all iframes
    iframes = driver.find_elements_by_tag_name('iframe')
    # Loop through iframes and try to find the button
    for iframe in iframes:
        driver.switch_to.frame(iframe)
        try:
            audio_challenge_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, 'recaptcha-audio-button'))
            )
            audio_challenge_button.click()
            print("Clicked the button")
            break  # If the button is clicked, break the loop
        except (TimeoutException, NoSuchElementException):
            print("Button not found in this frame, checking the next one.")
        driver.switch_to.default_content()  # Switch back to main content before checking next iframe

    driver.switch_to.default_content()


for i in range(1, 2):
    URL = 'https://www.google.com/recaptcha/api2/demo'
    create_account(URL)
    print(f"Account {i} is made")
