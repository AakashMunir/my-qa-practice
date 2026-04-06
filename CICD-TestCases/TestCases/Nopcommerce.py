# Nopcommerce.py - Pytest style mein convert karein
import pytest
import time
from playwright.sync_api import Page

def test_nopcommerce_login(page: Page):
    page.goto("https://gourmetfoods.pk/login")
    time.sleep(10)
    page.wait_for_selector("#mobile")
    page.locator("#mobile").fill("03136326900")
    page.locator("#password").fill("Malik0313")
    page.get_by_role("button", name="Login").click()
    # time.sleep(8)
    # page.locator("//body/div[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]").fill("Aakash")
    # page.locator('//*[@id="Password"]').fill("Malik0313")
    # page.locator('//*[@id="main"]/div/section/div/div[2]/div[1]/div[2]/form/div[2]/button').click()
    time.sleep(8)
#
