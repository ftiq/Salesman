{
    'name': 'Sales Visit Manager',
    'version': '18.0.1.0.0',
    'summary': 'Module to manage sales representative visits and permissions',
    'description': 'Module for managing sales visits, permissions, and related documents.',
    'author': 'Your Company',
    'depends': ['base', 'sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/sales_visit_views.xml',
        'views/res_partner_views.xml',
        'views/account_move_views.xml',
        'views/account_payment_views.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}