# Copyright (c) 2013, www.ossph.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
#from frappe.website.website_generator import WebsiteGenerator

class RepairOrder(Document):
	pass

def check_portal_enabled(reference_doctype):
	if not frappe.db.get_value('Portal Menu Item',
		{'reference_doctype': reference_doctype}, 'enabled'):
		frappe.throw(_("Request for Quotation is disabled to access from portal, for more check portal settings."))

def get_list_context(context=None):
	from erpnext.controllers.website_list_for_contact import get_list_context
	list_context = get_list_context(context)
	list_context["show_sidebar"] = True
	return list_context
