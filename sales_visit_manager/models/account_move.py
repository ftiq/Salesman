from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    salesman_id = fields.Many2one('res.users', string='Salesman')