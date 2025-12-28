from .Dashboard import Dashboard


class Login:

    def __init__(self, page):
        self.page = page
        self.mail=page.get_by_placeholder("email@example.com") # locator info

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def logginin(self, email, pwd):
        self.mail.fill(email)    # We can follow this approach for all locators
        self.page.locator("#userPassword").fill(pwd)
        self.page.locator("#login").click()
        das = Dashboard(self.page)
        return das

    # Adding this line to check git push and pull
