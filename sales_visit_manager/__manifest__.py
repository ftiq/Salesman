# sales_visit_manager/__manifest__.py
{
    'name': 'Sales Visit Manager',
    'version': '18.0.1.0.0',
    'summary': 'Manage sales representative visits and permissions',
    'description': 'تخزين وتتبع زيارات المندوبين مع التحكم في صلاحياتهم.',
    'author': 'Your Company',
    'category': 'Sales',
    'license': 'LGPL-3',
    'application': True,
    'depends': ['base', 'sale_management', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_sales_visit.xml',
        'views/sales_visit_views.xml',
        'views/res_partner_views.xml',
        'views/account_move_views.xml',
        'views/account_payment_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
