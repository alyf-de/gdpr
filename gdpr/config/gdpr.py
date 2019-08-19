# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("GDPR"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Processing Activity",
                    "label": _("Processing Activity"),
                    "description": _("Processing Activity")
                },
                {
                    "type": "doctype",
                    "name": "Technical and Organisational Measure",
                    "label": _("Technical and Organisational Measure"),
                    "description": _("Technical and Organisational Measure")
                }
            ]
        },
        {
            "label": _("Setup"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Data Recipient Category",
                    "label": _("Data Recipient Category"),
                    "description": _("Data Recipient Category")
                },
                {
                    "type": "doctype",
                    "name": "Storage Life",
                    "label": _("Storage Life"),
                    "description": _("Storage Life")
                },
                {
                    "type": "doctype",
                    "name": "Legal Basis",
                    "label": _("Legal Basis"),
                    "description": _("Legal Basis")
                },
                {
                    "type": "doctype",
                    "name": "Data Processing Purpose",
                    "label": _("Data Processing Purpose"),
                    "description": _("Data Processing Purpose")
                },
                {
                    "type": "doctype",
                    "name": "Personal Data Category",
                    "label": _("Personal Data Category"),
                    "description": _("Personal Data Category")
                },
                {
                    "type": "doctype",
                    "name": "Data Protection Guarantee",
                    "label": _("Data Protection Guarantee"),
                    "description": _("Data Protection Guarantee")
                }
            ]
        }
    ]
