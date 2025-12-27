from .SignoutPage import SignoutPage


class orderhist:
    def __init__(self, page):
        self.page = page


    def vieworder(self,orde_id):
        req_row = self.page.locator("tr").filter(has_text=orde_id)
        req_row.get_by_role("button", name="View").click()
        sign=SignoutPage(self.page)
        return sign