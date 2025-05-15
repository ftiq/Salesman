# models/salesman_daily_route_line.py
from odoo import models, fields

class SalesmanDailyRouteLine(models.Model):
    _name = 'salesman.daily.route.line'
    _description = 'تفاصيل خط السير اليومي'
    _order = 'sequence, day'

    daily_route_id = fields.Many2one(
        'salesman.daily.route', string='خط السير', required=True, ondelete='cascade')
    sequence = fields.Integer(string='الترتيب')
    day = fields.Selection([
        ('mon','الإثنين'),
        ('tue','الثلاثاء'),
        ('wed','الأربعاء'),
        ('thu','الخميس'),
        ('fri','الجمعة'),
        ('sat','السبت'),
        ('sun','الأحد'),
    ], string='اليوم', required=True)

    route_id = fields.Many2one(
        'salesman.route', string='المسار', required=True,
        help='اختر المسار أو المنطقة لهذا اليوم')
    active = fields.Boolean(
        string='مفعّل', default=True,
        help='إذا كانت هذه الزيارة ضمن الخطة')
