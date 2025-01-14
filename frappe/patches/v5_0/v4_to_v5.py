# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

import frappe

def execute():
	changed = (
		("desk", ("feed", "event", "todo", "note")),
		("custom", ("custom_field", "custom_script", "customize_form",
			 "customize_form_field", "property_setter")),
		("email", ("email_queue", "notification", "notification_recipient", "standard_reply")),
		("geo", ("country", "currency")),
		("print", ("letter_head", "print_format", "print_settings"))
	)
	for module in changed:
		for doctype in module[1]:
			frappe.reload_doc(module[0], "doctype", doctype)
