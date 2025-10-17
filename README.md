PROJECT SETUP STEPS

1. Install Python
   - Make sure Python 3.9 or above is installed on your system.
   - To check, open Command Prompt and type:
     python --version

2. (Optional) Create a Virtual Environment
   - Command:
     python -m venv venv
   - Activate it:
     venv\Scripts\activate    (for Windows)
     source venv/bin/activate (for macOS/Linux)

3. Install Required Libraries
   - Command:
     pip install playwright pytest
   - Then install browsers for Playwright:
     playwright install

------------------------------------------------------------
HOW TO RUN TEST CASES

To run a single test file:
   pytest tests/test1_login.py -s

To run all tests together:
   pytest -s

To run a specific test function from a file:
   pytest tests/test3_search_user.py::test_search_user -s

------------------------------------------------------------
TEST SCENARIOS AUTOMATED

1. Login - Verify admin login with valid credentials
2. Add User - Add a new user in User Management
3. Search User - Search for an existing user
4. Edit User - Edit user details (John → John Akhil Smith)
5. Validate User - Verify edited user appears in search
6. Delete User - Delete an existing user
7. Logout - Validate successful logout
8. Invalid Login - Validate system behavior for wrong credentials

------------------------------------------------------------
TECHNOLOGY STACK

Language: Python
Automation Tool: Playwright
Test Runner: Pytest
Browser: Chromium (default)

------------------------------------------------------------
PLAYWRIGHT VERSION DETAILS

Playwright Version: 1.45.0
Python Version: 3.10 or above

------------------------------------------------------------
AUTHOR DETAILS

Name: Ummar Farooq
Project: OrangeHRM Automation
Organization: Demo Automation Assignment

------------------------------------------------------------
NOTES

- Ensure your internet connection is active before running tests.
- Each test opens and closes its own browser session.
- To run tests in headless (background) mode, edit the script and change:
     browser = p.chromium.launch(headless=True)

------------------------------------------------------------
EXAMPLE RUN

Command:
   pytest tests/test4_edit_user.py -s

Expected Output:
    User 'John Smith' edited to 'John Akhil Smith' successfully!
------------------------------------------------------------
    



Bugs / Issues Summary

1. User Addition Issue:
When adding a new user, some valid usernames are rejected as invalid, while others are accepted without issue.


2. Edit Functionality Issue:
When changing a user’s status from Enabled to Disabled, the system shows a success message, but the user remains Enabled after refreshing the page.


3. User Deletion Issue:
Only certain users are getting deleted successfully — others remain in the list even after showing a success notification.


4. Intermittent Page Refresh Issue:
Occasionally, the Admin module or User Management page takes a long time to reload after performing actions like Add or Ed
