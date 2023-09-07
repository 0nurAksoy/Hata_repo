# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    _description = "Basic Inheritance"

    proje = fields.Selection([('a','A'),('b','B'),('c','C')], string='Seçiniz')
