# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Esto es un modulo de desmostracion para la clases de Industria del Software""",

    'description': """
        Es un modulo creado para aprender a usar Odoo
    """,

    'author': "UNAH",
    'website': "unah.edu.hn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'security/security.xml',
        'views/templates.xml',
        'views/course.xml',
        'views/session.xml',
        'views/partner.xml',
        #'views/wizard.xml',
        #'views/session_board.xml',
        #'reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
