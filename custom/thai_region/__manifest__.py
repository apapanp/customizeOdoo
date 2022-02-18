# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Thai Region Management',
    'version' : '1.0',
    'summary': 'Thai Region Management Software',
    'sequence': 10,
    'description': """ Thai Region Management Software  """,
    'category': 'Productivity',
    'website': 'https://www.odooair.com',
    'license': 'LGPL-3',
    'depends' : ['sale','base','http_routing',],
    'data': [
        'security/ir.model.access.csv',
        'views/regions.xml',
        'views/sale.xml',
        'views/users.xml',
    ],
    'demo': [],
    'qweb':[],
    'installable': True,
    'application': True,
    'auto_install': True,
    
}
