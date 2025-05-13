from odoo import models, fields

class SalesmanProfile(models.Model):
    _name = 'salesman.profile'
    _description = 'بطاقة المندوب'

    name = fields.Char(string='اسم المندوب', required=True)
