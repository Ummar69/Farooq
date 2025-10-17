from playwright.sync_api import sync_playwright

def test_validate_user():
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
        page.wait_for_selector("div.oxd-table-body")
        result_text = page.locator("div.oxd-table-body").inner_text()
        assert "John Akhil Smith" in result_text
        print("✅ User 'John Akhil Smith' validated successfully!")
        browser.close()

test_validate_user()