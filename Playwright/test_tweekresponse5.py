from playwright.sync_api import Page
fakepayloadres= {"data":[],"message":"No Orders"}
def intercept_res(route):
    route.fulfill(json=fakepayloadres) # deleting the actual response and passing this fake one


def test_tweekapplicationdata(page : Page):
    page.goto("https://rahulshettyacademy.com/client")

    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*",intercept_res)
    ## this above code is defined here, it will keep on listening from this step whenver this url call happens then it will activate and pas the fake response to browser
    page.get_by_placeholder("email@ex"
                            "ample.com").fill("rahulshetty@gmail.com")
    page.locator("#userPassword").fill("Iamking@000")
    page.locator("#login").click()

    page.get_by_role("button", name="ORDERS").click() # above route url activated once it reaches here

    print(page.locator(".mt-4").text_content())

    ######### This is 51st ledture,,,, watch 52 for another menthod route.continue_()#########

    ######### And 53rd lecture for injecting token to browser ########