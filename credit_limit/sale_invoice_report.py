from frappe import _

def execute(filters=None):
    """
    This function generates the data for the report based on the given filters.
    """
    columns = [
        _("Invoice No") + ":Link/Sale Invoice:120",
        _("Customer") + ":Link/Customer:120",
        _("Amount") + ":Currency:120",
        _("Status") + ":Data:120",
        # Add more columns as per your requirements
    ]

    data = get_invoice_data(filters)  # Implement your logic to fetch the invoice data

    return columns, data

def get_invoice_data(filters):
    """
    This function retrieves the invoice data based on the given filters.
    You can implement your own logic to fetch the data from the database.
    """
    # Implement your logic here to query the database and fetch the invoice data
    # Example:
    data = frappe.db.sql("""
        SELECT
            name AS invoice_no,
            customer,
            amount,
            status
        FROM
            `tabSale Invoice`
        WHERE
            %s
        ORDER BY
            name ASC
    """ % get_conditions(filters), as_dict=True)

    return data

def get_conditions(filters):
    """
    This function generates the SQL conditions based on the given filters.
    """
    conditions = ""
    # Implement your logic here to generate the SQL conditions based on the filters
    # Example:
    if filters.get("customer"):
        conditions += "customer = '%s'" % filters.get("customer")

    return conditions