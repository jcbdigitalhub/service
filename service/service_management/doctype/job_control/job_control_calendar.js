// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.views.calendar["Job Control"] = {
	field_map: {
		"start": "planned_start_date",
		"end": "planned_end_date",
		"id": "name",
		"title": "description",
		"allDay": "allDay"
	},
	gantt: true,
	get_css_class: function(data) {
		if(data.status==="Completed") {
			return "success";
		} else if(data.status==="In-Process") {
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
	get_events_method: "service.service_management.doctype.job_control.job_control.get_events"
}
