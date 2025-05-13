{
    'name': 'Salesman Backend',
    'version': '1.0',
    'summary': 'إدارة المناديب والمسارات',
    'description': 'نظام متكامل لإدارة فرق المبيعات الميدانية',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'category': 'Sales',
    'depends': ['base', 'sale', 'account', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/salesman_views.xml',  # يجب أن يكون قبل menu_views.xml
        'views/route_views.xml',
        'views/daily_route_views.xml',
        'views/daily_route_line_views.xml',
        'views/visit_views.xml',
        'views/res_partner_views.xml',
        'views/account_payment_views.xml',
        'views/menu_views.xml',  # يجب أن يكون الأخير
    ],
    'demo': [
        'demo/salesman_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'salesman_backend/static/src/css/salesman.css',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
