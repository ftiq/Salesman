from odoo import models, fields

class SalesVisit(models.Model):
    _name = 'sales.visit'
    _description = 'Sales Visit'

    visit_date = fields.Datetime(string='Visit Date')
    visit_type = fields.Selection([
        ('invoice', 'Invoice'),
        ('receipt', 'Receipt'),
        ('sales_order', 'Sales Order'),
        ('delivery', 'Delivery'),
        ('marketing', 'Marketing Activity'),
        ('cancelled', 'Cancelled Visit'),
    ], string='Visit Type')
    partner_id = fields.Many2one('res.partner', string='Customer')
    salesman_id = fields.Many2one('res.users', string='Salesman')
    invoice_id = fields.Many2one('account.move', string='Invoice')
    payment_id = fields.Many2one('account.payment', string='Payment')
    order_id = fields.Many2one('sale.order', string='Sales Order')
    delivery_done = fields.Boolean(string='Delivery Done')
    cancel_reason = fields.Char(string='Cancellation Reason')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], string='State', default='draft')