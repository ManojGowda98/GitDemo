import json
from pathlib import Path

import pytest
from playwright.sync_api import Playwright

from Playwright.Page_Objects.Login import Login
from Playwright.Utils.API_Framework_file import APIutilsFramwork

BASE_DIR = Path(__file__).parent
data_path= BASE_DIR /"Data/Credintials.json"

with open(data_path) as f:  # Path to JSON file
    test_data = json.load(f)  # Loading JSon into python object
    print(test_data)
    user_cred=test_data["credintials"]  # From JSon loading credintials part


@pytest.mark.parametrize("user_cred_passing",user_cred)
def test_web_api(playwright:Playwright,browser_instance,user_cred_passing):# user_cred_passing should be same as above(I think so)

    email=user_cred_passing["useremail"]
    pwd=user_cred_passing["password"]

    ########################### API ############npm -v###########
    orde_id = APIutilsFramwork().createorder(playwright,user_cred_passing)  # This file is connected with APU_base.py file and return order ID
    print(orde_id)

    ##########################Login Page ###################
    loginpage=Login(browser_instance)
    loginpage.navigate()
    das=loginpage.logginin(email,pwd)

    ########################## Dashboard ####################
    orderhistorypage=das.orderscreen()

    ########################## orderhistory ####################
    signout=orderhistorypage.vieworder(orde_id)

    ########################## Signout ####################
    signout.validatepage()

    # page.goto("https://rahulshettyacademy.com/client")
    # page.get_by_placeholder("email@example.com").fill(email)
    # page.locator("#userPassword").fill(pwd)
    # page.locator("#login").click()
