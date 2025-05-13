{
    'name': 'Sales Visit Manager',
    'version': '18.0.1.0.0',
    'summary': 'Manage sales representative visits and permissions',
    'description': 'Module for managing sales visits, permissions, and related operations.',
    'author': 'Your Company',
    'category': 'Sales',              # ← تأكد من وجود فئة مناسبة
    'application': True,              # ← هذا يجعل الموديول يظهر في لوحة التطبيقات
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
    'license': 'LGPL-3',
}
