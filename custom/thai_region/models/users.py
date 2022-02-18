# -*- coding: utf-8 -*-
from odoo import api, fields, models
class ResUser(models.Model):
    _inherit = "res.users"
    shop_name = fields.Char(string='Shop Name')
    regions = fields.Selection([
        ('Central', 'ภาคกลาง'),
        ('Eastern', 'ภาคตะวันออก'),
        ('Northeastern', 'ภาคตะวันออกเฉียงเหนือ'),
        ('Northern', 'ภาคเหนือ'),
        ('Southern', 'ภาคใต้'),
        ('Western', 'ภาคตะวันตก'),
        ('Bangkok Metropolitan ', 'กรุงเทพมหานครและปริมณฑล'),
    ])