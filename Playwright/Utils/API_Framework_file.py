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

class APIutilsFramwork:

    def login(self,playwright:Playwright,user_cred_passing):
        api_request_content= playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_content.post(url="/api/ecom/auth/login",
                                 data={
    "userEmail":user_cred_passing["useremail"],
    "userPassword":user_cred_passing["password"]
})
        if not response.ok:
            print(f"Login failed for {user_cred_passing['useremail']}: {response.text()}")
        assert response.ok
        body=response.json()
        return body["token"]

    def createorder(self,playwright:Playwright,user_cred_passing):
        token=self.login(playwright,user_cred_passing)
        api_request_content=playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response=api_request_content.post(url="/api/ecom/order/create-order",
                                 data=order_payload,
                                 headers={"Authorization":token,
                                          "content-type":"application/json"})
        print(response.json())
        res_body=response.json()
        ord_id= res_body["orders"][0]
        return ord_id