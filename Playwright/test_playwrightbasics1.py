import time

import pytest
from playwright.sync_api import Page,Playwright, expect


def test_playwrightbasics(playwright):
    browser=playwright.chromium.launch(headless=False)  
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://rahulshettyacademy.com/")

def test_playwrightshortcut(page:Page):
    page.goto("https://rahulshettyacademy.com/")

def test_corelocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy") # Username: here is a field name(label)
    page.get_by_label("Password:").fill("learningg") # Password: here is a field name(label)
    page.get_by_role("combobox").select_option("teach") # selecting role as combobox and choosing the value name defined in html(not the one which is displayed in UI)
    page.locator("#terms").check()  #clicking on T&C checkbox using CSS selector, #id and .classname
    page.get_by_role("link", name="terms and conditions").click() # clicking on T&C link, if many link are there in a page provide the correct link name in "name" key
    page.get_by_role("button",name="Sign In").click() # clicking on Sign in button, if many buttons are there in a page provide the correct button name in "name" key
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()  # Expect will wait automatically and to be visible is like assertion
    time.sleep(10)

################# Same file run in Firefox browser#############
@pytest.mark.skip
def test_edgeplaywright(playwright:Playwright):
    page=playwright.firefox.launch(headless=False).new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learningg")
    page.get_by_role("combobox").select_option(
        "teach")
    page.locator("#terms").check()
    page.get_by_role("link",
                     name="terms and conditions").click()
    page.get_by_role("button",
                     name="Sign In").click()
    expect(page.get_by_text(
        "Incorrect username/password.")).to_be_visible()
    time.sleep(10)