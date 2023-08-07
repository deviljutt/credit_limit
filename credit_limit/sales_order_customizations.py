# sales_order_customizations.py
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import msgprint
from frappe import throw
import sys
import logging
from datetime import datetime



def sales_order_on_submit(doc, method):
    doctype = "Credit Limit Settings"

    customer_name = doc.customer
    customer = frappe.get_doc("Customer", doc.customer)

    user = frappe.get_doc("User", frappe.session.user)
    user = user.email

    if user == "admin@example.com":
        return        


    if customer.credit_limits:
        credit_limit = customer.credit_limits[0].credit_limit
    else:
        credit_limit = None

    ordertotal = doc.total

    docz = frappe.get_doc(doctype, doctype)  
    
    om_profile = docz.om_profile
    ar_profile = docz.ar_profile
    ar_vp = docz.ar_vp
    ceo_profile = docz.ceo_profile


    price_level_one = int(docz.price_level_one)
    price_level_two = int(docz.price_level_two)
    price_level_three = int(docz.price_level_three)

    
   
    
    exists = None

    if credit_limit is not None:
        xx = credit_limit-ordertotal
        if xx <= 0:
            xx = abs(xx)
            if xx < price_level_one:
                approval_role = "Level 1"
                csv_values = ar_profile
                value_array = csv_values.split(",")
                value_to_check = user
                if value_to_check in value_array:
                    exists = "approve"
                else:
                    exists = "Only AR Profiles can approve"
            
            elif xx < price_level_two:
                approval_role = "Level 2"
                csv_values = ar_vp
                value_array = csv_values.split(",")
                value_to_check = user
                if value_to_check in value_array:
                    exists = "approve"
                else:
                    exists = "Only AR-VP can approve"

            elif xx < price_level_three:
                approval_role = "CEO"
                csv_values = ceo_profile
                value_array = csv_values.split(",")
                value_to_check = user
                if value_to_check in value_array:
                    exists = "approve"
                else:
                    exists = "Only CEO Profiles can approve"

        else:
            csv_values = om_profile
            value_array = csv_values.split(",")
            value_to_check = user
            if value_to_check in value_array:
                exists = "approve"
            else:
                exists = "Only OM Profiles can approve"

    if exists is not None and exists != 'approve':
        converted_string = str(exists) 
        throw(converted_string)            
    else:
        pass 
          
    
def sales_invoice_on_submit(doc, method):
        pass 
    


def seconds_to_days(seconds):
    days = seconds // 86400
    return days

def get_credit_days(customer_name):
    customer = frappe.get_doc("Customer", customer_name)
    payment_term_template_name = customer.payment_terms

    credit_days = None
    if payment_term_template_name:
        payment_terms_template = frappe.get_doc("Payment Term", payment_term_template_name)
        zzzzz = payment_terms_template.credit_days
        return zzzzz
    

def get_date_difference_from_last_sale_invoice(customer_name):
    invoices = frappe.get_all(
        "Sales Invoice",
        filters={"customer": customer_name, "docstatus": ["in", [1]]},
        fields=["posting_date", "docstatus"],
        order_by="posting_date desc",
        limit_page_length=1 
    )

    if invoices:
        last_invoice = invoices[0]
        posting_date = last_invoice.posting_date
        date_difference = datetime.now().date() - posting_date
        return date_difference.days
    else:
        return 0
