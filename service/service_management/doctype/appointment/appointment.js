// Copyright (c) 2016, www.ossph.com and contributors
// For license information, please see license.txt

frappe.ui.form.on('Appointment', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on("Appointment", "refresh", function(frm) {
        if(!frm.doc.__islocal) {
                frm.add_custom_button(__("Repair Estimate"), function() {
					frappe.model.open_mapped_doc({
						method: "service.service_management.doctype.appointment.appointment.make_repair_estimate",
						frm: cur_frm
						})                    
                }, __("Make"));
				cur_frm.page.set_inner_btn_group_as_primary(__("Make"));

                
				frm.add_custom_button(__("Repair Estimate"), function() {
                        frappe.route_options = {
                                appointment: frm.doc.name
                        }
                        frappe.set_route("List", "Repair Estimate");
                }, __("View"));
				
				frm.add_custom_button(__("Repair Order"), function() {
                        frappe.route_options = {
                                appointment: frm.doc.name
                        }
                        frappe.set_route("List", "Repair Order");
                }, __("View"));
				cur_frm.page.set_inner_btn_group_as_primary(__("View"));


        }
});
