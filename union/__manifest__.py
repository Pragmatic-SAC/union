# -*- coding: utf-8 -*-
{
    # App information
    'name': 'Union',
    'summary': 'Productos Union.',
    'version': '15.0.1',
    'category': 'Tools',
    'license': 'OPL-1',
    'website': 'https://www.pragmatic.com.pe/',
    'contributors': [
        'Kelvin Meza <kmeza@pragmatic.com.pe>',
    ],
    'depends': [
        'jwt_provider'
    ],
    'external_dependencies': {},
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/union_transporter.xml',
        'views/union_transporter_menu.xml',
    ],
    'images': [
    ],
    'qweb': [
    ],

    'author': 'Pragmatic S.A.C',
    'website': 'pragmatic.com.pe',
    'maintainer': 'Pragmatic S.A.C.',
    'installable': True,
    'auto_install': False,
    'application': True,
}
