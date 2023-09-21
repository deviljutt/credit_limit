from erpnext.controllers.selling_controller import SellingController
from erpnext.controllers.stock_controller import StockController


class updatesellingconrtoller(SellingController):
    def calculate_contribution(self):
        if not self.meta.get_field("sales_team"):
            return