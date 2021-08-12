from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Case"),
			"items": [
				{
					"type": "doctype",
					"name": "Case",
					"onboard": 1,
				},				
				{
					"type": "doctype",
					"name": "Case Log",
					"onboard": 1,
				}
			]
		},
		{
			"label": _("Legal Setting"),
			"items": [
				{
					"type": "doctype",
					"name": "Case Type",
				},
				{
					"type": "doctype",
					"name": "Legal Party",
				},
				{
					"type": "doctype",
					"name": "Lawyer",
				},
				{
					"type": "doctype",
					"name": "Case Level",
				},
			]
		}
	]