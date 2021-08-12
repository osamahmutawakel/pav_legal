from __future__ import unicode_literals

from frappe import _


def get_data():
	return {
		'fieldname': 'case_type',
		'transactions': [
			{
				'label': _('Case'),
				'items': ['Case']
			}
		]
	}
