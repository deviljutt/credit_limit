import frappe
import sys
import logging
from datetime import datetime


def sales_order_on_submit(doc, method):
    if doc.marketplace_order_number:
        existing_order = frappe.db.exists("Sales Order", filters={"marketplace_order_number": doc.marketplace_order_number}, fields=["name"])
        if existing_order:
            frappe.throw("Sales Order already exists for this marketplace order number: {}".format(doc.marketplace_order_number))
        else:
            pass