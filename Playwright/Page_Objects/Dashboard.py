from .orderhistory import orderhist


class Dashboard:
    def __init__(self,page):
        self.page=page

    def orderscreen(self):
        self.page.get_by_role("button", name="ORDERS").click()
        orderdata=orderhist(self.page)
        return orderdata