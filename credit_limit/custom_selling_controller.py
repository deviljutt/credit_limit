from erpnext.controllers.selling_controller import SellingController


class updatesellingconrtoller(SellingController):
    def calculate_contribution(self):
        if not self.meta.get_field("sales_team"):
            return