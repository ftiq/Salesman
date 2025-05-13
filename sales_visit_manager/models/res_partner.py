# sales_visit_manager/models/res_partner.py
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    salesman_id = fields.Many2one('res.users', string='Assigned Salesman')
