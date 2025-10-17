from playwright.sync_api import sync_playwright

def test_edit_user_john():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/")
        page.wait_for_selector('input[name="username"]')
        page.fill('input[name="username"]', "Admin")
        page.fill('input[name="password"]', "admin123")
        page.click('button[type="submit"]')
        page.wait_for_selector("text=Admin")
        page.click("text=Admin")
        page.wait_for_selector('input[placeholder="Username"]')
        page.fill('input[placeholder="Username"]', "John")
        page.click("button:has-text('Search')")
        page.wait_for_selector("xpath=(//i[@class='oxd-icon bi-pencil-fill'])[1]")
        page.click("xpath=(//i[@class='oxd-icon bi-pencil-fill'])[1]")
        page.wait_for_selector("//label[text()='Employee Name']/following::input[1]")
        page.fill("//label[text()='Employee Name']/following::input[1]", "John Akhil Smith")
        page.click("button:has-text('Save')")
        page.wait_for_selector("text=Successfully Updated")
        print("✅ User 'John Smith' edited to 'John Akhil Smith' successfully!")
        browser.close()

test_edit_user_john()