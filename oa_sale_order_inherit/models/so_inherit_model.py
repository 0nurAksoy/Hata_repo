# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrderInheritance(models.Model):
    _name = "sale.order.inherit"
    _inherit = ['sale.order']
    _description = "Sale Order Inheritance"

    # proje = fields.Many2one(comodel_name='project.project', ondelete='cascade')
    # task = fields.Many2one(comodel_name='project.task', ondelete='cascade')

    test = fields.Char(string='test', ondelete='cascade')