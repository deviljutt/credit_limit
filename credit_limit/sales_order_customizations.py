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


    if customer.credit_limits:
        credit_limit = customer.credit_limits[0].credit_limit
    else:
        credit_limit = 0
        
        
    saleorders = frappe.db.get_list('Sales Order', filters={ 'customer': doc.customer,'status': ['in', ['To Deliver and Bill','To Deliver','Completed']] }, fields=['total']); 
    total_amount = 0
    for entry in saleorders:
        total_amount += entry.get('total', 0)
    
       
       
    ordertotal = doc.total    
    credit_limit =  credit_limit - total_amount


    docz = frappe.get_doc(doctype, doctype)  
    
    om_profile = docz.om_profile.split(",")   
    ar_profile = docz.ar_profile.split(",")   
    ar_vp = docz.ar_vp.split(",")   
    ceo_profile = docz.ceo_profile.split(",")   


    price_level_one = docz.price_level_one
    price_level_two = docz.price_level_two
    price_level_three = docz.price_level_three
    
    exists = None
    role = None


    if credit_limit is not None: 
        xx = credit_limit
        if credit_limit <= 0:  
            credit_limit = abs(credit_limit)
            xx = abs(xx)  
            if user in om_profile:
                lower_bound, upper_bound = map(int, price_level_one.split('-'))
                if lower_bound <= xx <= upper_bound:
                    exists = "approve"
                    role = "om Profile"
            if user in ar_profile:
                lower_bound, upper_bound = map(int, price_level_two.split('-'))
                if lower_bound <= xx <= upper_bound:
                    exists = "approve"
                    role = "AR Profile"
            if user in ar_vp:
                lower_bound, upper_bound = map(int, price_level_three.split('-'))
                if lower_bound <= xx <= upper_bound:
                    exists = "approve"
                    role = "AR VP"
            if user in ceo_profile:
                exists = "approve"
                role = "ceo"
                 
        else:
            pass
    
        
        
        
    if exists != 'approve':
        converted_string = f'Credit Limit difference is {xx}. Contact upper-level permissions.'
        throw(converted_string)
    else:
        pass
    
    # customer_name = doc.customer
    # customer = frappe.get_doc("Customer", doc.customer)
    # user = frappe.get_doc("User", frappe.session.user)
    # user = user.email


    # posting_date = doc.transaction_date
    # date_object = datetime.strptime(posting_date, "%Y-%m-%d")
    # posting_date = datetime.timestamp(date_object)


    # current_datetime = datetime.now()
    # timestamp = datetime.timestamp(current_datetime)


    # time_difference =  timestamp - posting_date
    # days = int(seconds_to_days(time_difference))

    # credit_term = get_credit_days(customer_name)
    # if credit_term is None:
    #     return

    # doctype = "Credit Limit Settings"
    # docz = frappe.get_doc(doctype, doctype)  
    # om_profile = docz.om_profile
    # ar_profile = docz.ar_profile
    # ar_vp = docz.ar_vp
    # ceo_profile = docz.ceo_profile
    # outstandingdays = get_date_difference_from_last_sale_invoice(customer_name);
    # credit_term_one = int(docz.credit_term_one)
    # credit_term_two = int(docz.credit_term_two)
    # credit_term_three = int(docz.credit_term_three)
    # credit_term_four = int(docz.credit_term_four)

    # xx = int(credit_term) - int(outstandingdays) 
    # xx = abs(xx)


    # if xx > credit_term_four:
    #     approval_role = "CEO"
    #     csv_values = ceo_profile
    #     value_array = csv_values.split(",")
    #     value_to_check = user
    #     if value_to_check in value_array:
    #         exists = "approve"
    #     else:
    #         exists = "Credit Term: Only CEO can approve"
    
    # elif xx > credit_term_three:
    #     approval_role = "AR-VP"
    #     csv_values = ar_vp
    #     value_array = csv_values.split(",")
    #     value_to_check = user
    #     if value_to_check in value_array:
    #         exists = "approve"
    #     else:
    #         exists = "Credit Term: Only AR-VP can approve"


    # elif xx > credit_term_two:
    #     approval_role = "Level 2"
    #     csv_values = ar_profile
    #     value_array = csv_values.split(",")
    #     value_to_check = user
    #     if value_to_check in value_array:
    #         exists = "approve"
    #     else:
    #         exists = "Credit Term: Only AR Profile can approve"

    # elif xx > credit_term_one:
    #     approval_role = "Level 1"
    #     csv_values = om_profile
    #     value_array = csv_values.split(",")
    #     value_to_check = user
    #     if value_to_check in value_array:
    #         exists = "approve"
    #     else:
    #         exists = "Credit Term: Only OM Profile can approve"
    

    
          
    
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
