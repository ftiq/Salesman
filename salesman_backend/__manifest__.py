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
        'security/ir_rule.xml',  # تم نقل الملف إلى مجلد security
        'views/menu_views.xml',
        'views/salesman_views.xml',
        'views/route_views.xml',
        'views/daily_route_views.xml',
        'views/visit_views.xml',
        'views/res_partner_views.xml',
        'views/account_payment_views.xml',
    ],
    'demo': [
        'demo/salesman_demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'salesman_backend/static/src/css/salesman.css',
        ],
    },
    'installable': True
