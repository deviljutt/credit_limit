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
