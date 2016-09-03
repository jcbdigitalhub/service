// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.views.calendar["Appointment"] = {
	field_map: {
		"start": "appointment_date",
		"end": "appointment_date",
		"id": "name",
		"title": "serial_no",
		"allDay": "allDay"
	},
	gantt: true,
	get_css_class: function(data) {
		if(data.status==="Completed") {
			return "success";
		} else if(data.status==="In Process") {
			return "warning";
		} else {
			return "danger";
		}
	},
	filters: [
/*
		{
			"fieldtype": "Link",
			"fieldname": "sales_order",
			"options": "Sales Order",
			"label": __("Sales Order")
		},
*/
	],
	get_events_method: "service.service_management.doctype.appointment.appointment.get_events"
}
