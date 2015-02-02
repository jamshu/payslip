from openerp.osv import fields,osv,orm
from openerp.tools.translate import _
import base64
import csv
import StringIO
from datetime import datetime


def process_csv_data(csv_data):
		csv_data_lines=base64.decodestring(csv_data).replace("\r","").split("\n")
		res = []
		for line in csv_data_lines[1:]:
			
			if line:
				line_vals = line.split(',')
				res.append({
	                    'emp_id':line_vals[1],
	                    'employee_id':line_vals[2],
	                    'department_id':line_vals[3],
	                    'designation':line_vals[4],
	                    'bank_name':line_vals[5],
	                    'account_no':line_vals[6],
	                    'pan_no':line_vals[7],
	                    'regular_earnings':line_vals[15],
	                    'overtime_allowance':line_vals[16],
	                    'outstation_allowance':line_vals[17],
	                    'other_allowance':line_vals[18],
	                    'total_earnings':line_vals[19],
	                    'lop':line_vals[20],
	                    'tds':line_vals[21],
	                    'esi':line_vals[22],
	                    'professional_tax':line_vals[23],
	                    'kscea':line_vals[24],
	                    'pf':line_vals[25],
	                    'other_deductions':line_vals[26],
	                    'total_deductions':line_vals[27],
	                    'net_salary':line_vals[28],
 	                   
	                    })
		return res
class psimport_wiz(osv.osv_memory):
	_name = 'psimport.wiz'
	_columns = {
		
        'file_csv':fields.binary('Select the .CSV file', filters='*.csv'),
        'month':fields.selection([('01','January'), ('02','February'), ('03','March'), ('04','April'), ('05','May'), ('06','June'),
                                  ('07','July'), ('08','August'), ('09','September'), ('10','October'), ('11','November'), ('12','December')],'Month'),
		'year': fields.selection([(num, str(num)) for num in range(2000, (datetime.now().year)+1 )], 'Year'),
			}
	
	def do_import_csv(self, cr, uid, ids, context=None):
		data = self.browse(cr, uid, ids)[0]
		model_pool = self.pool.get('cs.payslip')
		if not data.file_csv:
			raise osv.except_osv(_('Warning'), _('File not selected !'))
		data_list = process_csv_data(data.file_csv)
		
		for vals in data_list:
			vals.update({'month':data.month,'year':data.year})
			model_pool.create(cr, uid, vals, context=context)
		return True
psimport_wiz()
