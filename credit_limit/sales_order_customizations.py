# sales_order_customizations.py
import frappe
from frappe import _
from frappe.model.document import Document
from frappe import msgprint
from frappe import throw
import sys





def sales_order_on_submit(doc, method):
    doctype = "Credit Limit Settings"

    customer_name = doc.customer
    customer = frappe.get_doc("Customer", doc.customer)

    user = frappe.get_doc("User", frappe.session.user)
    user = user.email
  

    if customer.credit_limits:
        credit_limit = customer.credit_limits[0].credit_limit
    else:
        credit_limit = None

    ordertotal = doc.total

    docz = frappe.get_doc(doctype, doctype)  
    
    om_profile = docz.om_profile
    ar_profile = docz.ar_profile
    ar_vp = docz.ar_vp


    price_level_one = int(docz.price_level_one)
    price_level_two = int(docz.price_level_two)
    price_level_three = int(docz.price_level_three)


    if credit_limit is not None:
        xx = credit_limit-ordertotal;
        exists = None;
        if xx < 0:
            xx = abs(xx)


            if xx > price_level_three:
                approval_role = "CEO"
                csv_values = ar_vp
                value_array = csv_values.split(",")
                value_to_check = user
                if value_to_check in value_array:
                    exists = "approve"
                else:
                    exists = "Only CEO can approve"
            elif xx > price_level_two:
                approval_role = "Level 2"
                csv_values = ar_profile
                value_array = csv_values.split(",")
                value_to_check = user
                if value_to_check in value_array:
                    exists = "approve"
                else:
                    exists = "Only Level 2 can approve"
            elif xx > price_level_one:
                approval_role = "Level 1"
                csv_values = om_profile
                value_array = csv_values.split(",")
                value_to_check = user
                if value_to_check in value_array:
                    exists = "approve"
                else:
                    exists = "Only Level 1 can approve"
            elif xx > 0:
                exists = None;


        else:
            pass   


        if exists is not None and exists != 'approve':
            converted_string = str(exists) 
            throw(converted_string)
        else:
            pass 
          

  

    

