import time

from playwright.sync_api import expect
from playwright.sync_api import Playwright

from Utils.API_Base import APIutils

## open API_Base.py file as well to undertand better##

def test_e2e_with_api(playwright:Playwright):
    Browser=playwright.chromium.launch(headless=False)
    context=Browser.new_context()
    page=context.new_page()

    orde_id=APIutils().createorder(playwright)  # This file is connected with APU_base.py file and return order ID
    print(orde_id)
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.locator("#userPassword").fill("Iamking@000")
    page.locator("#login").click()


    ##################Checking the order ID###########

    page.get_by_role("button", name="ORDERS").click()  # clicking order CTA
    req_row=page.locator("tr").filter(has_text=orde_id)  # getting the row where the order whuch we created throgh API is present in the table
    req_row.get_by_role("button",name="View").click()  # clicking on that specific row View button
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us") # validating last line message
    time.sleep(5)