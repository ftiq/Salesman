{
    'name': 'Salesman Backend',
    'version': '18.0.1.0',
    'data': [
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/menu_views.xml',
        'views/salesman_views.xml',
        'views/route_views.xml', 
        'views/daily_route_views.xml',
        'views/visit_views.xml',
        'views/res_partner_views.xml',
        'views/account_payment_views.xml',
        'demo/salesman_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'salesman_backend/static/src/css/salesman.css',
        ],
    },
    # ... باقي الإعدادات ...
}
