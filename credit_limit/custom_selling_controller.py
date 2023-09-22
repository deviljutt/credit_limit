import frappe
from frappe import _, bold, throw
from frappe.contacts.doctype.address.address import get_address_display
from frappe.utils import cint, flt, get_link_to_form, nowtime

from erpnext.controllers.accounts_controller import get_taxes_and_charges
from erpnext.controllers.sales_and_purchase_return import get_rate_for_return
from erpnext.controllers.stock_controller import StockController
from erpnext.stock.doctype.item.item import set_item_default
from erpnext.stock.get_item_details import get_bin_details, get_conversion_factor
from erpnext.stock.utils import get_incoming_rate
from erpnext.controllers.selling_controller import SellingController

class updatesellingconrtoller(SellingController):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __setup__(self):
        self.flags.ignore_permlevel_for_fields = ["selling_price_list", "price_list_currency"]

    def calculate_contribution(self):
        return