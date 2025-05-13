from odoo import models, fields

class SalesmanProfile(models.Model):
    _name = 'salesman.profile'
    _description = 'بطاقة المندوب'

    name = fields.Char(string='اسم المندوب', required=True)
    
    # يمكن إضافة الحقول الأخرى لاحقاً بعد التأكد من عمل الأساسيات
    # mobile = fields.Char(string='موبايل')
    # branch = fields.Many2one('res.branch', string='الفرع')
    # customer_ids = fields.Many2many('res.partner', string='العملاء')
    # route_ids = fields.One2many('salesman.route', 'salesman_id', string='المسارات')
