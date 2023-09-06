# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrderİnheritance(models.Model):
    _name = "sale.order.inherit"
    _inherit = ['project.project', 'project.task']
    _description = "Sale Order İnheritance"

    # proje = fields.Many2one(comodel_name='project.project', ondelete='cascade')
    # task = fields.Many2one(comodel_name='project.task', ondelete='cascade')

    test = fields.Many2one(string='name', ondelete='cascade')