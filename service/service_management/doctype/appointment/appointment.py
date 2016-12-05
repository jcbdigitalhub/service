# -*- coding: utf-8 -*-
# Copyright (c) 2015, www.ossph.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import frappe.utils
from frappe.utils import cstr, flt, getdate, comma_and, cint
from frappe import _
from frappe.model.mapper import get_mapped_doc
from frappe.model.document import Document

class Appointment(Document):
	pass

@frappe.whitelist()
def get_events(start, end, filters=None):
        """Returns events for Gantt / Calendar view rendering.

        :param start: Start date-time.
        :param end: End date-time.
        :param filters: Filters (JSON).
        """
        from frappe.desk.calendar import get_event_conditions
        conditions = get_event_conditions("Appointment", filters)

        data = frappe.db.sql("""select name, serial_no, appointment_date,
                appointment_date, status
                from `tabAppointment`
                where ((ifnull(appointment_date, '0000-00-00')!= '0000-00-00') \
                                and (appointment_date between %(start)s and %(end)s) \
                        or ((ifnull(appointment_date, '0000-00-00')!= '0000-00-00') \
                                and appointment_date between %(start)s and %(end)s)) {conditions}
                """.format(conditions=conditions), {
                        "start": start,
                        "end": end
                }, as_dict=True, update={"allDay": 0})
        return data

@frappe.whitelist()
def make_repair_estimate(source_name, target_doc=None):
		doc = get_mapped_doc("Appointment", source_name, {
			"Appointment": {
				"doctype": "Repair Estimate",
				"validation": {
					"docstatus": ["=",0]},
				"field_map":{
					"customer": "customer",
					"serial_no": "serial_no"}
				}
			},target_doc, postprocess=None)
		return doc