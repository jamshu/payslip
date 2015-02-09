from openerp.osv import fields,osv
from datetime import datetime
class cs_payslip(osv.osv):
	_name = 'cs.payslip'
	_description = 'Cs Payslip'
	_inherit = ['mail.thread']
	_columns = {
		'name':fields.char('Name',readonly=True),
		'emp_id':fields.char('Employee ID'),
		'employee_id':fields.char('Employee Name'),
		'department_id':fields.char('Department'),
		'designation':fields.char('Designation'),
		'bank_name':fields.char('Bank Name'),
		'account_no':fields.char('Bank A/C No'),
		'pan_no':fields.char('PAN No'),
		'regular_earnings':fields.float('Regular Earnings'),
		'overtime_allowance':fields.float('Overtime Allowance'),
		'outstation_allowance':fields.float('Outstation Allowance'),
		'other_allowance':fields.float('Other Allowance'),
		'total_earnings':fields.float('Total Earnings'),
		'tds':fields.float('TDS'),
		'esi':fields.float('ESI'),
		'professional_tax':fields.float('Professional Tax'),
		'kscea':fields.float('KSCEA'),
		'lop':fields.float('LOP'),
		'pf':fields.float('PF'),
		'other_deductions':fields.float('Other Deductions'),
		'total_deductions':fields.float('Total Deductions'),
		'net_salary':fields.float('Net Salary'),
		
		'month':fields.selection([('01','January'), ('02','February'), ('03','March'), ('04','April'), ('05','May'), ('06','June'),
                                  ('07','July'), ('08','August'), ('09','September'), ('10','October'), ('11','November'), ('12','December')],'Month'),
		'year': fields.selection([(num, str(num)) for num in range(2000, (datetime.now().year)+1 )], 'Year'),
			}
	_defaults = {
				 'name': lambda obj, cr, uid, context: '/',
				}
	def create(self, cr, uid, vals, context=None):
		if context is None:
			context = {}
		if vals.get('name', '/') == '/':
			vals['name'] = self.pool.get('ir.sequence').get(cr, uid, 'cs.payslip') or '/'
		return super(cs_payslip,self).create(cr, uid, vals, context=context)
cs_payslip()
