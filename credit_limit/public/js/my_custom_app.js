frappe.pages['my-custom-settings'] = {
  title: __('My Custom Settings'),
  parent: 'Setup',
  icon: 'fa fa-cogs',
  onload: function(wrapper) {
    wrapper.page.set_title(__('My Custom Settings'));
    // Add your custom settings HTML and logic here
  }
};
