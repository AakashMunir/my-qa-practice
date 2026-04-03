# Nopcommerce.py - Pytest style mein convert karein
import pytest
import time
from playwright.sync_api import Page

def test_nopcommerce_login(page: Page):
    page.goto("https://demo.nopcommerce.com/login?returnUrl=%2F")
    time.sleep(15)
    page.locator('//*[@id="Email"]').fill("mailk@mailk.com")
    page.locator('//*[@id="Password"]').fill("Malik0313")
    page.locator('//*[@id="main"]/div/section/div/div[2]/div[1]/div[2]/form/div[2]/button').click()
    time.sleep(8)

