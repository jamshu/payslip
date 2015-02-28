# -*- coding: utf-8 -*-
{

	'name': 'Payslip',
	'version': '1.0',
	'category': 'Production',
	'sequence': 1,
	'summary': 'Payslip',
	'author': 'Jamshid K<jamshu.mkd@gmail.com>',
	'website': 'https://www.intconsyst.com',
	'depends': ['base','mail','account'],
	'data': ['views/menu.xml',
			
			'views/psimport_wiz.xml',
			'views/cs_payslip.xml',
			'views/report_payslip.xml',
			'views/payslip_report.xml',
			'data/payslip_seq.xml',
			],
	'demo': [],
	'test': [],
	'installable': True,
	'auto_install': False,
	'application': True,

}
