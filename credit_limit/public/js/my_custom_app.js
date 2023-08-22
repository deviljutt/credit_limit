frappe.ui.form.on('Customer', {
  shipping_suppliers: function (frm) {
      var link_value = frm.doc.shipping_suppliers;
      if (link_value) {
        frappe.call({
            method: 'frappe.client.get',
            args: {
                doctype: 'Supplier',
                name: link_value
            },
            callback: function (response) {
                if (response.message) {
                    var linked_doc = response.message;
                    firsvalue = linked_doc.supplier_names;
                    frm.set_value('shipping_name', firsvalue);   
                }
            }
        });
    }
  }
});

frappe.ui.form.on('Sales Order', {
  customer: function (frm) {
      var link_value = frm.doc.customer;
      if (link_value) {
        frappe.call({
            method: 'frappe.client.get',
            args: {
                doctype: 'Customer',
                name: link_value
            },
            callback: function (response) {
                if (response.message) {
                    var linked_doc = response.message;
                    shipping_supplier = linked_doc.shipping_suppliers;
                    shipping_name = linked_doc.shipping_name;
                    shipping_detail = linked_doc.shipping_detail;

                    frm.set_value('shipping_supplier', shipping_supplier);   
                    frm.set_value('shipping_names', shipping_name);  
                    frm.set_value('shipping_phone', shipping_detail);  

                }
            }
        });
    }
  }
});


frappe.ui.form.on('Sales Invoice', {
  customer: function (frm) {
      var link_value = frm.doc.customer;
      if (link_value) {
        frappe.call({
            method: 'frappe.client.get',
            args: {
                doctype: 'Customer',
                name: link_value
            },
            callback: function (response) {
                if (response.message) {
                    var linked_doc = response.message;
                    shipping_supplier = linked_doc.shipping_supplier;
                    shipping_name = linked_doc.shipping_name;
                    shipping_detail = linked_doc.shipping_detail;

                    frm.set_value('shipping_suppliers', shipping_suppliers);   
                    frm.set_value('shipping_names', shipping_name);  
                    frm.set_value('shipping_detail', shipping_detail);  

                }
            }
        });
    }
  }
});



frappe.ui.form.on('Delivery Note', {
  customer: function (frm) {
      var link_value = frm.doc.customer;
      if (link_value) {
        frappe.call({
            method: 'frappe.client.get',
            args: {
                doctype: 'Customer',
                name: link_value
            },
            callback: function (response) {
                if (response.message) {
                    var linked_doc = response.message;
                    shipping_supplier = linked_doc.shipping_supplier;
                    shipping_name = linked_doc.shipping_name;
                    shipping_detail = linked_doc.shipping_detail;

                    frm.set_value('shipping_suppliers', shipping_supplier);   
                    frm.set_value('shipping_names', shipping_name);  
                    frm.set_value('shipping_detail', shipping_detail);  

                }
            }
        });
    }
  }
});
