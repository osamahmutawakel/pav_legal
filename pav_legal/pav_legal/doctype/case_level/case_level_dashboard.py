from __future__ import unicode_literals

from frappe import _


def get_data():
	return {
		'fieldname': 'case_level',
		'transactions': [
			{
				'label': _('Case Log'),
				'items': ['Case Log']
			}
		]
	}
