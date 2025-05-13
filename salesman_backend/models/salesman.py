from odoo import models, fields

class SalesmanProfile(models.Model):
    _name = 'salesman.profile'
    _description = 'بطاقة المندوب'

    name = fields.Char(string='اسم المندوب', required=True)
    mobile = fields.Char(string='موبايل')
    branch = fields.Many2one('res.branch', string='الفرع')
    
    # Permissions (صلاحيات متفرقة)
    allow_discount = fields.Boolean(string='السماح بالخصم')
    allow_price_edit = fields.Boolean(string='تعديل الأسعار')
    max_visits = fields.Integer(string='الحد الأقصى للزيارات')

    # Relations
    customer_ids = fields.One2many('res.partner', 'salesman_id', string='العملاء')
    payment_ids = fields.One2many('account.payment', 'salesman_id', string='قسائم الدفع')