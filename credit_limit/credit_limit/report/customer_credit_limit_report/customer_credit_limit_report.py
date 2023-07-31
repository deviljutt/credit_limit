# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt


import frappe
from frappe import _
from frappe.utils import flt

from erpnext.selling.doctype.customer.customer import get_credit_limit, get_customer_outstanding


def execute(filters=None):
	if not filters:
		filters = {}
	# Check if customer id is according to naming series or customer name
	customer_naming_type = frappe.db.get_value("Selling Settings", None, "cust_master_name")
	columns = get_columns(customer_naming_type)

	data = []

	customer_list = get_details(filters)

	for d in customer_list:
		row = []

		
		outstanding_amt = get_customer_outstanding(d.name, filters.get("company"))


		credit_limit = get_credit_limit(d.name, filters.get("company"))

		bal = flt(credit_limit) - flt(outstanding_amt)

		if customer_naming_type == "Naming Series":
			row = [
				d.name,
				credit_limit,
				outstanding_amt,
				d.cheque_amount,
				bal,
				d.is_frozen,
				d.disabled,
			]
		else:
			row = [
				d.name,
				credit_limit,
				outstanding_amt,
				d.cheque_amount,
				bal,
				d.is_frozen,
				d.disabled,
			]

		data.append(row)

	return columns, data


def get_columns(customer_naming_type):
	columns = [
		_("Customer") + ":Link/Customer:120",
		_("Credit Limit") + ":Currency:120",
		_("Outstanding Invoice") + ":Currency:100",
		_("Outstanding Cheque") + ":Currency:120",
		_("Credit Balance") + ":Currency:120",
		_("Is Frozen") + ":Check:80",
		_("Disabled") + ":Check:80",
	]

	if customer_naming_type == "Naming Series":
		columns.insert(1, _("Customer Name") + ":Data:120")

	return columns

def get_details(filters):

	sql_query = """
		SELECT
			name,
			customer_name,
			customer_group,
			territory,
			(SELECT SUM(paid_amount) FROM `tabPayment Entry` pe WHERE pe.party = c.name AND pe.mode_of_payment = 'Cheque' AND pe.docstatus = '1') AS cheque_amount,
			(SELECT COUNT(name) FROM `tabSales Order` so WHERE so.customer = c.name AND so.docstatus = '1') AS total_sales_orders
		FROM `tabCustomer` c
	"""
	

	# customer filter is optional.
	if filters.get("customer"):
		sql_query += " AND c.name = %(customer)s"

	return frappe.db.sql(sql_query, filters, as_dict=1)
