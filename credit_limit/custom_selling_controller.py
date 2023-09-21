from erpnext.controllers.selling_controller import SellingController

class updatesellingconrtoller(SellingController):
    def calculatecontribution(self):
        if not self.meta.get_field("sales_team"):
            return