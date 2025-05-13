# sales_visit_manager/models/account_payment.py
from odoo import models, fields

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    salesman_id = fields.Many2one('res.users', string='Salesman')
