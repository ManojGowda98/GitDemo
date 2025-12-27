import time

import pytest
from playwright.sync_api import Page, expect

######### Hide and Display #############
@pytest.mark.skip
def test_Uichecks(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible() # Asserting if this is visible or not
    page.locator("#hide-textbox").click()  # clicking on Hide button
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()# Asserting if this is hidden or not
    #time.sleep(5)


############### Alert Boxes ##############
    page.on("dialog",lambda dialog:dialog.accept()) # Handel alert and click on accept, A lambda is a small, anonymous (nameless) function written in one single line.
    page.get_by_role("button",name="Confirm").click()



############## Frames Handling ############

    page_frame=page.frame_locator("#courses-iframe")
    page_frame.get_by_text("Close", exact=True).click()
    page_frame.get_by_role("link",name="All-Access").click()
    expect(page_frame.locator("body")).to_contain_text("Unlimited Lifetime Access")

    ### SEE 40th lecture again


##########################################################
# Check the price of the Rice is equal to 37
#Identify the Price Col
#Identify the Rice row
#Extract the price of the Rice

def test_tableAndColValidation(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    col_name=page.locator("th").all_inner_texts() #Grabbing all the column text from table and assigngin to list
    print(col_name)    #Printing it
    for i in col_name:  # Looping with col_name
        if i=="Price":  # from col_name finding the Price coloumn
            print(i)
            break
    Ricerow=page.locator("tr").filter(has_text="Rice") # from the row filtering the Rice and assign to element var
    expect(Ricerow.locator("td").nth(col_name.index(i))).to_have_text("37") # from ricerow locator, findling all the values and getting only the Price index value and asserting it

################################# Gemini version of same above code##################
def test_tablevalid(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # 1. Wait for the headers to actually exist (Ensures table is loaded)
    header_locator = page.locator("th")
    header_locator.first.wait_for()

    # 2. Grab all names at once (Fast)
    col_names = header_locator.all_inner_texts()

    # 3. Use Python's built-in index finding
    try:
        price_idx = col_names.index("Price")

        # 4. Use the index to validate the specific row
        rice_row = page.locator("tr").filter(has_text="Rice")
        expect(rice_row.locator("td").nth(price_idx)).to_have_text("37")

    except ValueError:
        print("Could not find 'Price' column in the table!")
