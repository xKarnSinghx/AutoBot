import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select

SELECTORS = {
    "create_account": [
        "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-dgl2Hf ksBjEc lKxP2d LQeN7 FliLIb uRo0Xe TrZEUc Xf9GD']",
        "//*[@class='JnOM6e TrZEUc kTeh9 KXbQ4b']"
    ],
    'for_my_personal_use': [
        "//span[@class='VfPpkd-StrnGf-rymPhb-b9t22c']",
    ],
    "first_name": "//*[@name='firstName']",
    "last_name": "//*[@name='lastName']",
    "username": "//*[@name='Username']",
    "password": "//*[@name='Passwd']",
    "confirm_password": "//*[@name='ConfirmPasswd']",
    "next": [
        "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b']",
        "//button[contains(text(),'Next')]",
        "//button[contains(text(),'I agree')]"
    ],
    "phone_number": "//*[@id='phoneNumberId']",
    "code": '//input[@name="code"]',
    "acc_phone_number": '//input[@id="phoneNumberId"]',
    "acc_day": '//input[@name="day"]',
    "acc_month": '//select[@id="month"]',
    "acc_year": '//input[@name="year"]',
    "acc_gender": '//select[@id="gender"]',
    "username_warning": '//*[@class="jibhHc"]',
}


def click_checkbox(driver_obj):
    driver_obj.switch_to.default_content()
    driver_obj.switch_to.frame(driver_obj.find_element(By.XPATH, "//span[@class='laptop-desktop-only']"))
    driver_obj.find_element(By.ID, "laptop-desktop-only").click()
    driver_obj.switch_to.default_content()


def create_account(driver_obj):
    driver_obj.switch_to.default_content()
    driver_obj.find_element(By.XPATH, "//span[@class='laptop-desktop-only']").click()
    driver_obj.switch_to.default_content()


def basic_info(driver_obj):
    birthday = str(random.randint(1, 12)) + "/" + str(random.randint(1, 28)) + "/" + str(
        random.randint(1980, 1999))
    WebDriverWait(driver_obj, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="day"]'))).send_keys(
        str(random.randint(1, 27)))
    select_acc_month = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//select[@id="month"]')))

    acc_month = Select(select_acc_month)
    acc_month.select_by_value(birthday.split('/')[0])
    WebDriverWait(driver_obj, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="year"]'))).send_keys(
        str(random.randint(1950, 2005)))
    select_acc_gender = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//select[@id="gender"]')))

    acc_gender = Select(select_acc_gender)
    acc_gender.select_by_value('1')
    for selector in SELECTORS['next']:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, selector))).click()
            break
        except:
            pass


def make_account(driver_obj, first, last):
    driver_obj.switch_to.default_content()
    driver_obj.find_element(By.ID, "firstName").send_keys(first)
    driver_obj.switch_to.default_content()
    driver_obj.find_element(By.ID, "lastName").send_keys(last)
    driver_obj.switch_to.default_content()
    driver_obj.find_element(By.ID, "collectNameNext").click()
    driver_obj.switch_to.default_content()


def make_gmail(driver_obj, first_name, last_name):
    driver_obj.switch_to.default_content()
    try:
        my_choice = WebDriverWait(driver_obj, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="selectionc2"]')))
        my_choice.click()
    except:
        pass
    # my_choice = WebDriverWait(driver_obj, 10).until(
    #     EC.presence_of_element_located((By.XPATH, '//*[@id="selectionc2"]')))
    # my_choice.click()
    rand_5_digit_num = random.randint(10000, 99999)
    user_name = first_name + "." + last_name
    user_name = user_name.lower() + str(rand_5_digit_num)
    user_name_tag = WebDriverWait(driver_obj, 10).until(
        EC.presence_of_element_located((By.XPATH, SELECTORS['username'])))
    user_name_tag.clear()
    user_name_tag.send_keys(user_name)
    for selector in SELECTORS['next']:
        try:
            WebDriverWait(driver_obj, 10).until(EC.presence_of_element_located((By.XPATH, selector))).click()
            break
        except:
            pass


def generatePassword():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    size = random.randint(8, 12)
    return ''.join(random.choice(chars) for x in range(size))


def fill_pass(driver_obj):
    password = generatePassword()
    passwd_tag = WebDriverWait(driver_obj, 10).until(
        EC.presence_of_element_located((By.XPATH, SELECTORS['password'])))
    passwd_tag.send_keys(password)
    # time.sleep(10)
    confirmwd_tag = WebDriverWait(driver_obj, 10).until(
        EC.presence_of_element_located((By.NAME, 'PasswdAgain')))
    confirmwd_tag.send_keys(password)
    for selector in SELECTORS['next']:
        try:
            WebDriverWait(driver_obj, 10).until(EC.presence_of_element_located((By.XPATH, selector))).click()
            break
        except:
            pass
    time.sleep(10)


for i in range(1, 2):
    URL = 'https://www.google.com/gmail/about/'
    FIRST = f'test00{i}'
    LAST = 'mark'

    driver = webdriver.Firefox()
    driver.get(URL)
    create_account(driver)
    make_account(driver, FIRST, LAST)
    basic_info(driver)
    make_gmail(driver, FIRST, LAST)
    time.sleep(10)
    fill_pass(driver)
    print(f"Account {i} is made")
