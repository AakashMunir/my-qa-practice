# Nopcommerce.py - Pytest style mein convert karein
import pytest
import time
from playwright.sync_api import Page
import allure
@allure.feature("Login")
@allure.story("Successful Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_nopcommerce_login(page: Page):
    with allure.step("Navigate to login page"):
        page.goto("https://gourmetfoods.pk/login")
    time.sleep(10)
    with allure.step("Fill in credentials"):
        page.wait_for_selector("#mobile")
        page.locator("#mobile").fill("03136326900")
        page.locator("#password").fill("Malik0313")
    with allure.step("Click login button"):
        page.get_by_role("button", name="Login").click()
    time.sleep(8)
#
