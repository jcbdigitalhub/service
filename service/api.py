# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import json
from frappe import _
from frappe.model.mapper import get_mapped_doc

@frappe.whitelist()
def get_ro_checklist(quality_checklist):
	ck = frappe.get_list("Quality Checklist Item", fields=["code", "description"], filters={"parent": quality_checklist}, order_by= "idx")
	return ck

