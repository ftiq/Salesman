class SalesmanRoute(models.Model):
    _name = 'salesman.route'
    _description = 'مسار'

    name = fields.Char(string='اسم المسار', required=True)
    salesman_id = fields.Many2one('salesman.profile', string='المندوب')
    customer_ids = fields.Many2many('res.partner', string='العملاء')

class DailyRoute(models.Model):
    _name = 'salesman.daily.route'
    _description = 'خط السير اليومي'

    date = fields.Date(string='التاريخ', default=fields.Date.today)
    salesman_id = fields.Many2one('salesman.profile', string='المندوب')
    visit_ids = fields.One2many('salesman.visit.log', 'daily_route_id', string='الزيارات')