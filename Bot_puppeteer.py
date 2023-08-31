# import asyncio
# import pyppeteer
# from pyppeteer import launch
# from pyppeteer.errors import TimeoutError as PyppeteerTimeoutError, ElementHandleError
#
#
# async def create_account(url, email, password):
#     browser = await launch(headless=False)
#     # browser = await pyppeteer.launch()
#     page = await browser.newPage()
#
#     await page.goto(url)
#     try:
#         await page.waitForXPath("//span[contains(text(), 'Login')]", timeout=10000)
#         login_button = await page.xpath("//span[contains(text(), 'Login')]")
#         await login_button[0].click()
#
#         await page.waitForXPath("//span[contains(text(), 'Sign Up')]", timeout=10000)
#         signup_tab = await page.xpath("//span[contains(text(), 'Sign Up')]")
#         await signup_tab[0].click()
#
#         email_input = await page.evaluateHandle('''() => {
#                 const labels = document.querySelectorAll("label");
#                 for (const label of labels) {
#                     if (label.textContent.includes("Enter Email")) {
#                         return label.nextElementSibling.querySelector("input");
#                     }
#                 }
#                 return null;
#             }''')
#         await email_input.type(email)
#         password_input = await page.evaluateHandle('''() => {
#                 const labels = document.querySelectorAll("label");
#                 for (const label of labels) {
#                     if (label.textContent.includes("Enter Password")) {
#                         return label.nextElementSibling.querySelector("input");
#                     }
#                 }
#                 return null;
#             }''')
#         await password_input.type(password)
#
#         password_input = await page.evaluateHandle('''() => {
#                         const labels = document.querySelectorAll("label");
#                         for (const label of labels) {
#                             if (label.textContent.includes("Confirm Password")) {
#                                 return label.nextElementSibling.querySelector("input");
#                             }
#                         }
#                         return null;
#                     }''')
#         await password_input.type(password)
#
#         try:
#             await page.waitForXPath("//button/span[contains(text(), 'Sign Up')]", timeout=10000)
#             signup_button = await page.xpath("//button/span[contains(text(), 'Sign Up')]")
#             await signup_button[0].click()
#
#         except (PyppeteerTimeoutError, ElementHandleError):
#             print("Unsuccessful SignUp")
#
#         await asyncio.sleep(10)
#
#     finally:
#         await browser.close()
#
#
# for i in range(1, 10):
#     asyncio.get_event_loop().run_until_complete(
#         create_account('https://crypto-hunter.netlify.app/', f'test0{i}_email@example.com', 'test_password123'))
#     print(f"Made account {i}")

import asyncio
from pyppeteer import launch
from pyppeteer.errors import TimeoutError as PyppeteerTimeoutError, ElementHandleError


async def create_account(url, email, password, name):
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto(url)

    try:
        # await page.waitForXPath("//button[contains(text(), 'Join')]", timeout=10000)
        # join_button = await page.xpath("//button[contains(text(), 'Join')]")
        # await join_button[0].click()
        await page.waitForXPath("//button[contains(@class, 'sc-1ln0sw6-0 cmMSFw sc-1ekvrxa-18 hvsMAJ') and "
                                "contains(text(),'Join')]", timeout=10000)
        login_button = await page.xpath("//button[contains(@class, 'sc-1ln0sw6-0 cmMSFw sc-1ekvrxa-18 hvsMAJ') and "
                                        "contains(text(),'Join')]")
        await login_button[0].click()

        # await page.waitForXPath("//input[@id='name']", timeout=10000)
        # name_input = await page.xpath("//input[@id='name']")
        # await name_input[0].type(name)
        #
        # await page.waitForXPath("//input[@id='login_email']", timeout=10000)
        # email_input = await page.xpath("//input[@id='login_email']")
        # await email_input[0].type(email)
        #
        # await page.waitForXPath("//input[@id='password']", timeout=10000)
        # password_input = await page.xpath("//input[@id='password']")
        # await password_input[0].type(password)
        #
        # await page.waitForXPath("//div[contains(text(), 'Join with email')]", timeout=10000)
        # join_email_button = await page.xpath("//div[contains(text(), 'Join with email')]")
        # await join_email_button[0].click()
        #
        # await page.waitForXPath("//a[contains(text(), 'Skip')]", timeout=10000)
        # skip_button = await page.xpath("//a[contains(text(), 'Skip')]")
        # await skip_button[0].click()

    except (PyppeteerTimeoutError, ElementHandleError):
        print(f"Unsuccessful signup with {PyppeteerTimeoutError} and {ElementHandleError}")

    finally:
        await browser.close()


async def main():
    for i in range(1, 10):
        URL = 'https://vimeo.com'
        EMAIL = f'testx00{i}_email@example.com'
        PASSWORD = 'testX_password123'
        NAME = f'test{i}xyssys'

        await create_account(URL, EMAIL, PASSWORD, NAME)
        print(f"Account {i} is made")


asyncio.get_event_loop().run_until_complete(main())
