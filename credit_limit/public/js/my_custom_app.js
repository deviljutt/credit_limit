frappe.ui.form.on('Customer', {
    custom_shipping_supplier: function (frm) {
        var link_value = frm.doc.custom_shipping_supplier;
        if (link_value) {
          frappe.call({
            method: 'frappe.desk.form.load.getdoc',
              args: {
                  doctype: 'Supplier',
                  name: link_value
              },
              callback: function (response) {
                if(response.docs){
                  var doc = response.docs[0];
                  var address = '';
                  if(doc.__onload.addr_list){
                    address = doc.__onload.addr_list[0].city;
                  }
                  firsvalue = doc.supplier_names;
                  frm.set_value('shipping_name', firsvalue); 
                  frm.set_value('shipping_detail', address);
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
                    shipping_supplier = linked_doc.custom_shipping_supplier;
                    shipping_name = linked_doc.shipping_name;
                    shipping_detail = linked_doc.shipping_detail;

                    frm.set_value('shipping_suppliers', shipping_supplier);   
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
                    shipping_supplier = linked_doc.custom_shipping_supplier;
                    shipping_name = linked_doc.shipping_name;
                    shipping_detail = linked_doc.shipping_detail;

                    frm.set_value('shipping_suppliers', shipping_supplier);   
                    frm.set_value('shipping_names', shipping_name);  
                    frm.set_value('shipping_phone', shipping_detail);  

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
                    shipping_supplier = linked_doc.custom_shipping_supplier;
                    shipping_name = linked_doc.shipping_name;
                    shipping_detail = linked_doc.shipping_detail;

                    frm.set_value('shipping_suppliers', shipping_supplier);   
                    frm.set_value('shipping_names', shipping_name);  
                    frm.set_value('shipping_phone', shipping_detail);  

                }
            }
        });
    }
  }
});

frappe.ui.form.on('Packing Slip', {
    delivery_note: function (frm) {
        var link_value = frm.doc.delivery_note;
        if (link_value) {
          frappe.call({
            method: 'frappe.client.get',
              args: {
                  doctype: 'Delivery Note',
                  name: link_value
              },
              callback: function (response) {
				var address = response.message.customer_address;
				frm.set_value('customer_addresss', address); 
              }
          });
      }
    }
  });


frappe.ui.form.on('Sales Invoice', {
    onload: function (frm) {
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
						shipping_supplier = linked_doc.custom_shipping_supplier;
						shipping_name = linked_doc.shipping_name;
						shipping_detail = linked_doc.shipping_detail;

						frm.set_value('shipping_suppliers', shipping_supplier);   
						frm.set_value('shipping_names', shipping_name);  
						frm.set_value('shipping_phone', shipping_detail);  

					}
				}
			});
    }
	}
  });


frappe.ui.form.on('Delivery Note', {
    onload: function (frm) {
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
						shipping_supplier = linked_doc.custom_shipping_supplier;
						shipping_name = linked_doc.shipping_name;
						shipping_detail = linked_doc.shipping_detail;

						frm.set_value('shipping_suppliers', shipping_supplier);   
						frm.set_value('shipping_names', shipping_name);  
						frm.set_value('shipping_phone', shipping_detail);  

					}
				}
			});
    }
	}
  });


frappe.ui.form.on('Packing Slip Item', {
    package_qty: function(frm, cdt, cdn) {
        var item = frappe.get_doc(cdt, cdn);
        // Access the updated value
        var newQuantity = item.package_qty;

        // Perform your custom action here, e.g., recalculate totals, update UI, etc.
        // You can use the `frm` object to interact with the form's fields or perform actions.

        // Example: Recalculate total
        frm.doc.total_amount = frm.doc.items.reduce(function(acc, cur) {
            return acc + (cur.package_qty * cur.rate);
        }, 0);
        var total = 0;
        if(frm.doc.items){
            frm.doc.items.forEach((item) => {
                total += item.package_qty;
            });
        }
        frm.set_value('package_total', total);  
    }
});

frappe.ui.form.on('Delivery Note', {
    refresh: function (frm) {
        var deliveryNoteName = frm.doc.name;
        
        frappe.db.get_list('Packing Slip', {
            filters: {
                'delivery_note': deliveryNoteName
            }
        }).then(records => {
            var docname = records[0].name;
			
			
			frappe.call({
            method: 'frappe.desk.form.load.getdoc',
              args: {
                  doctype: 'Packing Slip',
                  name: docname
              },
              callback: function (response) {
                var items = response.docs[0].items;
                var packgtotal = response.docs[0].package_total;
	
		frm.clear_table('packing_slip_item');
		items.forEach(function (item) {
			var row = frm.add_child('packing_slip_item');
			row.item_code = item.item_code;
			row.item_name = item.item_name;
			row.qty = item.qty;
			row.package_qty = item.package_qty;
			row.package_uom = item.package_uom;
		}); 
		frm.set_value('package_s', packgtotal);   


		      
				
              }
			});
			
			
			
        });
    }
});
