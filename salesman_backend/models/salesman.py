from odoo import models, fields

class SalesmanProfile(models.Model):
    _name = 'salesman.profile'
    _description = 'بطاقة المندوب'

    name = fields.Char(string='اسم المندوب', required=True)
    mobile = fields.Char(string='موبايل')
    branch = fields.Many2one('res.branch', string='الفرع')
    active = fields.Boolean(default=True)
    
    # تعديل العلاقة لاستخدام نفس اسم الحقل
    customer_ids = fields.One2many(
        'res.partner',
        'salesman_id',  # يجب أن يتطابق مع اسم الحقل في res.partner
        string='العملاء'
    )
    payment_ids = fields.One2many('account.payment', 'salesman_id', string='قسائم الدفع')
    route_ids = fields.One2many('salesman.route', 'salesman_id', string='المسارات')
