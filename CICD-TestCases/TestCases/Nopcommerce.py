# Nopcommerce.py - Pytest style mein convert karein
import pytest
import time
from playwright.sync_api import Page

def test_nopcommerce_login(page: Page):
    page.goto("https://demo.nopcommerce.com/login?returnUrl=%2F")
    page.get_by_role("textbox", name="Email:").fill("mailk@mailk.com")
    page.get_by_role("textbox", name="Email:").press("Tab")
    page.get_by_role("textbox", name="Password:").fill("Malik0313")
    page.get_by_role("button", name="Log in").click()
    time.sleep(8)

