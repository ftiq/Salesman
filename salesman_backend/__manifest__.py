{
    'name': 'Salesman Backend',
    'version': '1.0',
    'summary': 'Manage salesmen, routes, and visits',
    'description': 'Custom backend for salesmen linked to mobile app',
    'category': 'Sales',
    'author': 'Your Company',
    'depends': ['base', 'sale', 'account'],  # Dependencies
    'data': [
        'security/ir.model.access.csv',
        'views/salesman_views.xml',
        'views/route_views.xml',
        'views/visit_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}