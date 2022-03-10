# -*- coding: utf-8 -*-
{
    'name': "tiendas",

    'summary': """
        Aquí encontrarás las mejores tiendas de fruta.""",

    'description': """
        Conjunto de tiendas a las que suministramos nuestras mejores frutas.
    """,

    'author': "Papaya S.L.",
    'website': "http://www.PapayaFrutas.com",

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
