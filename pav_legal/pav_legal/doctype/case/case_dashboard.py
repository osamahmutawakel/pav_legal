from __future__ import unicode_literals

from frappe import _


def get_data():
	return {
		'fieldname': 'case',
		'transactions': [
			{
				'label': _('Logs'),
				'items': ['Case Log']
			}
		]
	}
