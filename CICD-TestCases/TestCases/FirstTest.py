import re
import time
import os
from datetime import datetime
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://10.166.1.88/#login")
    time.sleep(15)
    page.get_by_role("textbox", name="Email address or Username").click()
    page.get_by_role("textbox", name="Email address or Username").fill("013076")
    page.get_by_role("textbox", name="Password").fill("@qwerty#123")
    page.get_by_role("button", name="Login with LDAP").click()
    time.sleep(8)
    # ------------------------
    # Add ne line
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)