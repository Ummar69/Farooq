from playwright.sync_api import sync_playwright

def test_delete_user():
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
        page.fill('input[placeholder="Username"]', "John Akhil Smith")
        page.click("button:has-text('Search')")
        page.wait_for_selector("xpath=(//i[@class='oxd-icon bi-trash'])[1]")
        page.click("xpath=(//i[@class='oxd-icon bi-trash'])[1]")
        page.wait_for_selector("button:has-text('Yes, Delete')")
        page.click("button:has-text('Yes, Delete')")
        page.wait_for_selector("text=Successfully Deleted")
        print("✅ User 'John Akhil Smith' deleted successfully!")
        browser.close()

test_delete_user()