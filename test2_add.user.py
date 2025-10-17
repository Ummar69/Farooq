from playwright.sync_api import sync_playwright

def test_add_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/")
        page.fill('input[name="username"]', "Admin")
        page.fill('input[name="password"]', "admin123")
        page.click('button[type="submit"]')
        page.click("text=Admin")
        page.click("text=Add")
        page.locator("xpath=//div[label[text()='User Role']]//i").click()
        page.locator("text=Admin").click()
        page.fill("input[placeholder='Type for hints...']", "a")
        page.locator("text=Alice Duval").click()
        page.locator("xpath=//div[label[text()='Status']]//i").click()
        page.locator("text=Enabled").click()
        page.fill("input[name='username']", "umar_demo")
        page.fill("input[name='password']", "Test@12345")
        page.fill("input[name='confirmPassword']", "Test@12345")
        page.click("button[type='submit']")
        browser.close()

test_add_user()