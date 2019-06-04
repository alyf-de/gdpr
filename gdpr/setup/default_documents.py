# -*- coding: utf-8 -*-
from frappe import _

def get_data():
    return [
        {
            "doctype": "Personal Data Category",
            "title": _("Address")
        },
        {
            "doctype": "Personal Data Category",
            "title": _("Birth Date")
        }
    ]
