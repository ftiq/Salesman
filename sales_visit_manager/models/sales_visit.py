from odoo import models, fields

class SalesVisit(models.Model):
    _name = 'sales.visit'
    _description = 'Sales Visit'
    _order = 'visit_date desc'

    visit_date     = fields.Datetime(string='Visit Date', required=True)
    visit_type     = fields.Selection([
        ('invoice',   'Invoice'),
        ('refund',    'Refund'),
        ('receipt',   'Receipt'),
        ('order',     'Sales Order'),
        ('delivery',  'Delivery'),
        ('marketing', 'Marketing Activity'),
        ('cancelled', 'Cancelled Visit'),
    ], string='Type', required=True)
    partner_id     = fields.Many2one('res.partner',   string='Customer',      required=True)
    salesman_id    = fields.Many2one('res.users',     string='Salesman',      required=True, default=lambda self: self.env.uid)
    invoice_id     = fields.Many2one('account.move',  string='Invoice')
    payment_id     = fields.Many2one('account.payment', string='Payment')
    order_id       = fields.Many2one('sale.order',    string='Sales Order')
    delivery_done  = fields.Boolean(string='Delivery Done')
    cancel_reason  = fields.Text(string='Cancellation Reason')
    state          = fields.Selection([
        ('draft',     'Draft'),
        ('done',      'Done'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='draft')

    def action_done(self):
        """Mark this visit as done."""
        self.write({'state': 'done'})

    def action_cancel(self):
        """Mark this visit as cancelled."""
        self.write({'state': 'cancelled'})
