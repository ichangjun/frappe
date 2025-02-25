# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt
import frappe
import os
from frappe.core.doctype.file.file import get_content_hash


def execute():
	frappe.reload_doc('core', 'doctype', 'file_data')
	for name, file_name, file_url in frappe.db.sql(
			"""select name, file_name, file_url from `tabFile`
			where file_name is not null"""):
		b = frappe.get_doc('File', name)
		old_file_name = b.file_name
		b.file_name = os.path.basename(old_file_name)
		if old_file_name.startswith('files/') or old_file_name.startswith('/files/'):
			b.file_url = os.path.normpath('/' + old_file_name)
		else:
			b.file_url = os.path.normpath('/files/' + old_file_name)
		try:
			_file = frappe.get_doc("File", {"file_name": name})
			content = _file.get_content()
			b.content_hash = get_content_hash(content)
		except IOError:
			print('Warning: Error processing ', name)
			_file_name = old_file_name
			b.content_hash = None

		try:
			b.save()
		except frappe.DuplicateEntryError:
			frappe.delete_doc(b.doctype, b.name)

