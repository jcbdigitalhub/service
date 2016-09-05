from __future__ import unicode_literals
from frappe import _

def get_data():
        return [
                {                
                        "label": _("Service Desk"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Appointment"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Repair Estimate"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Repair Order"
                                },
                                {
                                        "type": "doctype",
                                        "name": "RO Checklist"
                                },
                                
                        ]
                },
		{
                        "label": _("Shop Floor"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Job Control"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Technician Assignment"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Quality Control"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Technician"
                                },
                        ]
                },
                {
                        "label": _("Warranty and Insurance"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Warranty",
					"label": "Warranty Claim"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Warranty Processing"
                                },
                                {
                                        "type": "doctype",
                                        "name": "RO Insurance Claim",
					"label": "Insurance Claim"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Principal Entity"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Insurance Company"
                                },
                        ]
                },
                {
                        "label": _("Masters"),
                        "items": [
                                {
                                        "type": "doctype",
                                        "name": "Workshop"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Operations"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Diagnosis Codes"
                                },
                              
                                {
                                        "type": "doctype",
                                        "name": "Operations"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Service Advisor"
                                },
                                {
                                        "type": "doctype",
                                        "name": "Customer"
                                },

                                {
                                        "type": "doctype",
                                        "name": "Supplies"
                                }
                        ]
                },


	]
