from playwright.sync_api import Playwright
login_payload={
    "userEmail": "rahulshetty@gmail.com",
    "userPassword": "Iamking@000"
}

order_payload={
    "orders": [
        {
            "country": "India",
            "productOrderedId": "693d421832ed86587130ecee"
        }
    ]
}

class APIutils:

    def login(self,playwright:Playwright):
        api_request_content= playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_content.post(url="/api/ecom/auth/login",
                                 data=login_payload)
        assert response.ok
        body=response.json()
        return body["token"]

    def createorder(self,playwright:Playwright):
        token=self.login(playwright)
        api_request_content=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_content.post(url="/api/ecom/order/create-order",
                                 data=order_payload,
                                 headers={"Authorization":token,
                                          "content-type":"application/json"})
        print(response.json())
        res_body=response.json()
        ord_id= res_body["orders"][0]
        return ord_id