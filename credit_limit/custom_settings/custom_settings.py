from frappe import _

def get_data():
    return [
        {
            "label": _("Custom Settings"),
            "icon": "fa fa-cog",
            "items": [
                {
                    "type": "doctype",
                    "name": "Custom Settings",
                    "label": _("Custom Settings"),
                    "description": _("Custom Settings"),
                }
            ]
        }
    ]
