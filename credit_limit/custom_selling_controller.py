from erpnext.controllers.selling_controller import SellingController
from frappe.utils import flt


class updatesellingconrtoller():
    def calculatecontribution(self):
        if not self.meta.get_field("sales_team"):
            return