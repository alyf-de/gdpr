# -*- coding: utf-8 -*-
import frappe
from default_documents import get_data

def after_install():
    data = get_data()
    for doc in data:
        frappe.get_doc(doc).insert()
