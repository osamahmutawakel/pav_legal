from __future__ import unicode_literals

from frappe import _


def get_data():
	return {
		'fieldname': 'lawyer',
		'internal_links': {
			'Case': ['default_lawyer', 'lawyer'],
			'Case Log': ['lawyer', 'lawyer']
		},
	}
