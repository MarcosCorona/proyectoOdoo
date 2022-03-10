# -*- coding: utf-8 -*-
{
    'name': "tiendas",

    'summary': """
        Lista de tiendas que tenemos.
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Conjunto de tiendas a las que suministramos nuestras mejores frutas.
    """,

    'author': "Papaya S.L.",
    'website': "http://www.PapayaFrutas.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'The best',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True ,
}
