from . import __version__ as app_version
from frappe import _

app_name = "credit_limit"
app_title = "Credit Limit"
app_publisher = "zaviago"
app_description = "Credit Limit"
app_email = "nabeel@zaviago.com"
app_license = "MIT"

# Includes in <head>
# ------------------

#doc_events = {
#'Sales Order': {
#      'before_submit': 'credit_limit.sales_order_customizations.sales_order_on_submit'
#   }
#}

doc_events = {
'Sales Order': {
      'before_submit': 'credit_limit.saleordersubmitbefore.sales_order_on_submit',
	'before_save': 'credit_limit.saleordersubmitbefore.sales_order_on_submit'
   }
}

# include js, css files in header of desk.html
# app_include_css = "/assets/credit_limit/css/credit_limit.css"
# app_include_js = "/assets/credit_limit/js/credit_limit.js"
#app_include_js = "/assets/credit_limit/js/my_custom_app.js?"+"000777777"




# include js, css files in header of web template
# web_include_css = "/assets/credit_limit/css/credit_limit.css"
# web_include_js = "/assets/credit_limit/js/credit_limit.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "credit_limit/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "credit_limit.utils.jinja_methods",
#	"filters": "credit_limit.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "credit_limit.install.before_install"
# after_install = "credit_limit.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "credit_limit.uninstall.before_uninstall"
# after_uninstall = "credit_limit.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "credit_limit.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }


override_doctype_class = {
	"Custom Field": "credit_limit.custom_field.CustomField",
    #"Quotation": "credit_limit.custom_selling_controller.updatesellingconrtoller",
    #"Sales Order": "credit_limit.custom_sales_order.SalesOrder"
}

override_whitelisted_methods = {
	"erpnext.selling.doctype.quotation.quotation.make_sales_order": "credit_limit.custom_sales_order.custom_method_name"
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"credit_limit.tasks.all"
#	],
#	"daily": [
#		"credit_limit.tasks.daily"
#	],
#	"hourly": [
#		"credit_limit.tasks.hourly"
#	],
#	"weekly": [
#		"credit_limit.tasks.weekly"
#	],
#	"monthly": [
#		"credit_limit.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "credit_limit.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "credit_limit.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "credit_limit.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["credit_limit.utils.before_request"]
# after_request = ["credit_limit.utils.after_request"]

# Job Events
# ----------
# before_job = ["credit_limit.utils.before_job"]
# after_job = ["credit_limit.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"credit_limit.auth.validate"
# ]

