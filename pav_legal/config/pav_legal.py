from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Issues"),
			"items": [
				{
					"type": "doctype",
					"name": "Case",					
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Issue Type",
					"description": _("Issue Type."),
				},
				{
					"type": "doctype",
					"name": "Issue Priority",
					"description": _("Issue Priority."),
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
					"name": "Lawyer",					
				},
				{
					"type": "doctype",
					"name": "Prosecution",					
				},
				{
					"type": "doctype",
					"name": "Police Station",					
				},
				{
					"type": "doctype",
					"name": "Court",					
				},
			]
		}
	]