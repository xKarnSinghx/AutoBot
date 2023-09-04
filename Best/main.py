from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import requests
import whisper
import warnings

warnings.filterwarnings("ignore")

model = whisper.load_model("base")


def transcribe(url):
    with open('.temp', 'wb') as f:
        f.write(requests.get(url).content)
    result = model.transcribe('.temp')
    return result["text"].strip()


def click_checkbox(driver_obj):
    driver_obj.switch_to.default_content()
    driver_obj.switch_to.frame(driver_obj.find_element(By.XPATH, ".//iframe[@title='reCAPTCHA']"))
    driver_obj.find_element(By.ID, "recaptcha-anchor-label").click()
    driver_obj.switch_to.default_content()


def request_audio_version(driver_obj):
    driver_obj.switch_to.default_content()
    driver_obj.switch_to.frame(
        driver_obj.find_element(By.XPATH, ".//iframe[@title='recaptcha challenge expires in two minutes']"))
    driver_obj.find_element(By.ID, "recaptcha-audio-button").click()


def solve_audio_captcha(driver_obj):
    text = transcribe(driver_obj.find_element(By.ID, "audio-source").get_attribute('src'))
    driver_obj.find_element(By.ID, "audio-response").send_keys(text)
    driver_obj.find_element(By.ID, "recaptcha-verify-button").click()


def submit_button(driver_obj):
    driver_obj.switch_to.default_content()
    driver_obj.find_element(By.ID, "recaptcha-demo-submit").click()


if __name__ == "__main__":
    driver = webdriver.Firefox()

    driver.get("https://www.google.com/recaptcha/api2/demo")

    click_checkbox(driver)
    time.sleep(1)
    request_audio_version(driver)
    time.sleep(1)
    solve_audio_captcha(driver)
    time.sleep(5)
    submit_button(driver)
