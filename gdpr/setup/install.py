# -*- coding: utf-8 -*-
import frappe
from default_documents import get_data

def after_install():
    default_documents = get_data()
    for doc in default_documents:
        frappe.get_doc(doc).insert()
