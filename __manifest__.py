# -*- coding: utf-8 -*-
{
    'name': "hotelsge",

    'summary': "Gestión simplificada de las reservas de un hotel",

    'description': """
    Gestión simplificada de las reservas de un hotel. Aplicación que contará con numerosas funcionalidades.
    """,

    'author': "Tony",
    'website': "https://www.somosdelprieto.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/18.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/security.xml',
        'security/ir.model.access.csv',
        'views/cliente.xml',
         'views/review.xml',
        'views/habitacion.xml',
        'views/reserva.xml',
        'views/actions.xml',
        'views/menus.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

