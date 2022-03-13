# -*- coding: utf-8 -*-
{
<<<<<<< HEAD
    'name': "rutas",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",
=======
    'name': "Rutas",

    'summary': """
        Lista de rutas.""",

    'description': """
        Conjunto de rutas entre diferentes tiendas.
    """,

    'author': "Papaya S.L.",
    'website': "http://www.PapayaFrutas.com",
>>>>>>> 32f68800703ac4294af370149e9c76497b2b20d4

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
<<<<<<< HEAD
    'category': 'Uncategorized',
=======
    'category': 'The best',
>>>>>>> 32f68800703ac4294af370149e9c76497b2b20d4
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
<<<<<<< HEAD
        # 'security/ir.model.access.csv',
=======
        'security/rutas_security.xml',
        'security/ir.model.access.csv',
>>>>>>> 32f68800703ac4294af370149e9c76497b2b20d4
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
<<<<<<< HEAD
=======
    'application':True ,
>>>>>>> 32f68800703ac4294af370149e9c76497b2b20d4
}
