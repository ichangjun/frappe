
import frappe

def execute():
	frappe.reload_doctype("User")
	frappe.db.sql("update `tabUser` set last_active=last_login")
