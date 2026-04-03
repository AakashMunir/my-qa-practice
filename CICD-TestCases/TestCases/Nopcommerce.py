import re
import time
import os
from datetime import datetime
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.nopcommerce.com/login?returnUrl=%2F")
    page.get_by_role("textbox", name="Email:").fill("mailk@mailk.com")
    page.get_by_role("textbox", name="Email:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill("Malik0313")
    page.get_by_role("button", name="Log in").click()
    time.sleep(8)
    page.get_by_role("heading", name="demo.nopcommerce.com").click()
    time.sleep(8)
    # ---------------------
    # Add ne line
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)