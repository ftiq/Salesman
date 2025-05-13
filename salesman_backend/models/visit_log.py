class VisitLog(models.Model):
    _name = 'salesman.visit.log'
    _description = 'سجل الزيارات'

    salesman_id = fields.Many2one('salesman.profile', string='المندوب')
    customer_id = fields.Many2one('res.partner', string='العميل')
    date = fields.Datetime(string='تاريخ الزيارة', default=fields.Datetime.now)
    action = fields.Selection([
        ('invoice', 'فاتورة مبيعات'),
        ('payment', 'سند قبض'),
        ('failed', 'فشل الزيارة'),
    ], string='الإجراء')