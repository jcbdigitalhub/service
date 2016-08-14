// Copyright (c) 2015, Frappe Technologies and contributors
// For license information, please see license.txt

cur_frm.add_fetch("course", "course_code", "course_code");

frappe.ui.form.on("Repair Order", "refresh", function(frm) {
	if(!frm.doc.__islocal) {
		frm.add_custom_button(__("RO Checklist"), function() {
			frappe.route_options = {
				repair_order: frm.doc.name
			}
			frappe.set_route("List", "RO Checklist");
		});
		
		frm.add_custom_button(__("Quality Control"), function() {
			frappe.route_options = {
				repair_order: frm.doc.name
			}
			frappe.set_route("List", "Quality Control");
		});
		

	}
});
