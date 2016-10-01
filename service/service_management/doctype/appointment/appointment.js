// Copyright (c) 2016, www.ossph.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Appointment', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on("Appointment", "refresh", function(frm) {
        if(!frm.doc.__islocal) {
                frm.add_custom_button(__("Repair Estimate"), function() {
                        frappe.route_options = {
                                appointment: frm.doc.name
                        }
                        frappe.set_route("List", "Repair Estimate");
                });

                frm.add_custom_button(__("Repair Order"), function() {
                        frappe.route_options = {
                                appointment: frm.doc.name
                        }
                        frappe.set_route("List", "Repair Order");
                });


        }
});
