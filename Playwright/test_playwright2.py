import time

from playwright.sync_api import Page, expect


def test_UIvalidations(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link",name="terms and conditions").click()
    page.get_by_role("button",name="Sign In").click()
    Iphone=page.locator("app-card").filter(has_text="iphone X") # accessing whole card and selecting iphone by filtering it
    Iphone.get_by_role("button",name="Add").click() # once the Iphone card is accessed, click on Add button
    Nokia_Edge = page.locator("app-card").filter(has_text="Nokia Edge")
    Nokia_Edge.get_by_role("button", name="Add").click()
    page.get_by_text("Checkout").click()  # clicking on checkout button
    expect(page.locator(".media-body")).to_have_count(2) # Assertion whether only 2 card are selected or not
    time.sleep(10)


def test_childwindowhandles(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as new_page: # expecting child window from next page hence define before that next line
        page.locator(".blinkingText").click() # this click will open new window
        child_window=new_page.value      # storing the value of new window
        text=child_window.locator(".red").text_content()  # accessing childwindow and grabbing the text
        print(text)
        new1=text.split("at")[1].split("with")[0].strip() # splitting and stripping the text
        assert new1=="mentor@rahulshettyacademy.com"
