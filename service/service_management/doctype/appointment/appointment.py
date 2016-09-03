# -*- coding: utf-8 -*-
# Copyright (c) 2015, www.ossph.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
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

