{
    'name': 'Salesman Backend',
    'version': '1.0',
    'summary': 'إدارة المناديب والمسارات',
    'description': 'نظام متكامل لإدارة فرق المبيعات الميدانية',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'category': 'Sales',
    'depends': ['base', 'sale', 'account', 'contacts', 'stock'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'data': [
        # 🛡️ ملفات الصلاحيات أولاً
        'security/ir.model.access.csv',

        # 📄 Views التي تحتوي على actions
        'views/salesman_profile_view.xml',
        'views/salesman_route_views.xml',
        'views/salesman_daily_route_views.xml',
        'views/salesman_visit_log_views.xml',
        'views/sale_order_views.xml',
        'views/account_payment_views.xml',
        'views/account_move_views.xml',
        'views/stock_picking_views.xml',
        'views/stock_warehouse_views.xml',

        # 🧭 القوائم دائماً في النهاية
        'views/menu.xml',
    ],
}
