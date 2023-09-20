from erpnext.controllers.selling_controller import SellingController
from frappe.utils import flt

def calculate_contribution(self):
    if not self.meta.get_field("sales_team"):
        return

# Assign the custom function to the SellingController class
SellingController.calculate_contribution = calculate_contribution

