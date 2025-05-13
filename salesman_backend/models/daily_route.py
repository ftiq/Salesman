from odoo import models, fields

class DailyRoute(models.Model):
    _name = 'salesman.daily.route'
    _description = 'خط السير اليومي'

    name = fields.Char(string='الاسم', compute='_compute_name')
    date = fields.Date(string='التاريخ', required=True)
    salesman_id = fields.Many2one('salesman.profile', string='المندوب')
    route_line_ids = fields.One2many('salesman.daily.route.line', 'daily_route_id', string='العملاء')

    @api.depends('date', 'salesman_id')
    def _compute_name(self):
        for rec in self:
            rec.name = f"{rec.salesman_id.name or ''} - {rec.date}"
