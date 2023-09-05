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

    # customer_name = doc.customer
    # customer = frappe.get_doc("Customer", doc.customer)

    # user = frappe.get_doc("User", frappe.session.user)
    # user = user.email


    # if customer.credit_limits:
    #     credit_limit = customer.credit_limits[0].credit_limit
    # else:
    #     credit_limit = 0
        
        
    # saleorders = frappe.db.get_list('Sales Order', filters={ 'customer': doc.customer,'status': ['in', ['To Deliver and Bill','To Deliver','Completed']] }, fields=['total']); 
    # total_amount = 0
    # for entry in saleorders:
    #     total_amount += entry.get('total', 0)
    

    # ordertotal = doc.total    
    # credit_limit =  credit_limit - total_amount
    
    docz = frappe.get_doc(doctype, doctype)  
    
    om_profile = docz.om_profile.split(",")   
    ar_profile = docz.ar_profile.split(",")   
    ar_vp = docz.ar_vp.split(",")   
    ceo_profile = docz.ceo_profile.split(",")   


    # price_level_one = docz.price_level_one
    # price_level_two = docz.price_level_two
    # price_level_three = docz.price_level_three
    
    # exists = None
    # role = None


    # if credit_limit is not None: 
    #     xx = credit_limit-ordertotal

    #     if xx < 0:  
    #         xx = abs(xx)  
    #         if user in om_profile:
    #             lower_bound, upper_bound = map(int, price_level_one.split('-'))
    #             if lower_bound <= xx <= upper_bound:
    #                 exists = "approve"
    #                 role = "om Profile"
    #         if user in ar_profile:
    #             lower_bound, upper_bound = map(int, price_level_two.split('-'))
    #             if lower_bound <= xx <= upper_bound:
    #                 exists = "approve"
    #                 role = "AR Profile"
    #         if user in ar_vp:
    #             lower_bound, upper_bound = map(int, price_level_three.split('-'))
    #             if lower_bound <= xx <= upper_bound:
    #                 exists = "approve"
    #                 role = "AR VP"
    #         if user in ceo_profile:
    #             exists = "approve"
    #             role = "ceo"
                 
    #     else:
    #         exists = "approve"    
        

    # if exists != 'approve':
    #     converted_string = f'Credit Limit difference is {xx}. Contact upper-level permissions.'
    #     throw(converted_string)
    # else:
    #     pass
    
    customer_name = doc.customer
    customer = frappe.get_doc("Customer", doc.customer)
    user = frappe.get_doc("User", frappe.session.user)
    user = user.email


    posting_date = doc.transaction_date
    date_object = datetime.strptime(posting_date, "%Y-%m-%d")
    posting_date = datetime.timestamp(date_object)


    current_datetime = datetime.now()
    timestamp = datetime.timestamp(current_datetime)

    time_difference =  timestamp - posting_date
    days = int(seconds_to_days(time_difference))
    credit_term = get_credit_days(customer_name)
    if credit_term is None:
         credit_term = 7
    
    outstandingdays = get_date_difference_from_last_sale_invoice(customer_name);
    xx = int(credit_term) - int(outstandingdays) 

    exists = None
    role = None
    price_level_one = docz.credit_term_one
    price_level_two = docz.credit_term_two
    price_level_three = docz.credit_term_three

    if xx is not None: 
        if xx < 0:  
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
            exists = "approve" 

        converted_string = f'Credit Term difference is {xx}. Contact upper-level permissions. outstanding days is {outstandingdays} credit term days is {credit_term} {role}'
        throw(converted_string)


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
        filters={"customer": customer_name, "status": ["in", ['Overdue']]},
        fields=["posting_date","due_date"]
    )
    
    diff = []
    if invoices:
        for item in invoices:
            due_date = item['due_date']
            date_difference = datetime.now().date() - due_date
            diff.append(date_difference.days)
        
        maxz = max(diff)    
        return maxz
