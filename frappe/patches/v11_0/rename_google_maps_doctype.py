
import frappe
from frappe.model.rename_doc import rename_doc

def execute():
	if frappe.db.exists("DocType","Google Maps") and not frappe.db.exists("DocType","Google Maps Settings"):
		rename_doc('DocType', 'Google Maps', 'Google Maps Settings')
		frappe.reload_doc('integrations', 'doctype', 'google_maps_settings')