import asyncio
import pyppeteer
from pyppeteer import launch
from pyppeteer.errors import TimeoutError as PyppeteerTimeoutError, ElementHandleError


async def create_account(url, email, password):
    browser = await launch(headless=False)
    # browser = await pyppeteer.launch()
    page = await browser.newPage()

    await page.goto(url)
    try:
        await page.waitForXPath("//span[contains(text(), 'Login')]", timeout=10000)
        login_button = await page.xpath("//span[contains(text(), 'Login')]")
        await login_button[0].click()

        await page.waitForXPath("//span[contains(text(), 'Sign Up')]", timeout=10000)
        signup_tab = await page.xpath("//span[contains(text(), 'Sign Up')]")
        await signup_tab[0].click()

        email_input = await page.evaluateHandle('''() => {
                const labels = document.querySelectorAll("label");
                for (const label of labels) {
                    if (label.textContent.includes("Enter Email")) {
                        return label.nextElementSibling.querySelector("input");
                    }
                }
                return null;
            }''')
        await email_input.type(email)
        password_input = await page.evaluateHandle('''() => {
                const labels = document.querySelectorAll("label");
                for (const label of labels) {
                    if (label.textContent.includes("Enter Password")) {
                        return label.nextElementSibling.querySelector("input");
                    }
                }
                return null;
            }''')
        await password_input.type(password)

        password_input = await page.evaluateHandle('''() => {
                        const labels = document.querySelectorAll("label");
                        for (const label of labels) {
                            if (label.textContent.includes("Confirm Password")) {
                                return label.nextElementSibling.querySelector("input");
                            }
                        }
                        return null;
                    }''')
        await password_input.type(password)

        try:
            await page.waitForXPath("//button/span[contains(text(), 'Sign Up')]", timeout=10000)
            signup_button = await page.xpath("//button/span[contains(text(), 'Sign Up')]")
            await signup_button[0].click()

        except (PyppeteerTimeoutError, ElementHandleError):
            print("Unsuccessful SignUp")

        await asyncio.sleep(10)

    finally:
        await browser.close()


for i in range(1, 10):
    asyncio.get_event_loop().run_until_complete(
        create_account('https://crypto-hunter.netlify.app/', f'test0{i}_email@example.com', 'test_password123'))
    print(f"Made account {i}")
