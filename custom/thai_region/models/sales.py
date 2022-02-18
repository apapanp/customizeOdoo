# -*- coding: utf-8 -*-
from odoo import api, fields, models
class SaleOrder(models.Model):
    _inherit = "sale.order"
    shop_name = fields.Char(string='Shop Name', required=True)
    regions = fields.Selection([
        ('Central', 'ภาคกลาง'),
        ('Eastern', 'ภาคตะวันออก'),
        ('Northeastern', 'ภาคตะวันออกเฉียงเหนือ'),
        ('Northern', 'ภาคเหนือ'),
        ('Southern', 'ภาคใต้'),
        ('Western', 'ภาคตะวันตก'),
        ('Bangkok Metropolitan ', 'กรุงเทพมหานครและปริมณฑล'),
    ], required=True, default='Central')