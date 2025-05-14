{
    'name': 'Salesman Backend',
    'version': '1.0',
    'summary': 'إدارة المناديب والمسارات',
    'description': 'نظام متكامل لإدارة فرق المبيعات الميدانية',
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'category': 'Sales',
    'depends': ['base', 'sale', 'account', 'contacts'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'data': [
        'views/salesman_profile_view.xml',
        # أضف المزيد من ملفات الـ XML هنا إن وجدت
    ],
    'license': 'LGPL-3',
}
