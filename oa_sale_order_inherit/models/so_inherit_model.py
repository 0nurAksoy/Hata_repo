# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrderInheritance(models.Model):
    _name = "sale.order.inherit"
    _inherit = ['sale.order']
    _description = "Sale Order Inheritance"

    proje = fields.Many2one(comodel_name='project.project', ondelete='cascade')
    task = fields.Many2one(comodel_name='project.task', ondelete='cascade')

    user_ids = fields.Many2many(
        'project.task.user', 'task_user_rel',
        'task_id', 'user_id',
        string='User Ids')
    transaction_ids = fields.Many2many(
        'sale.order.transaction', 'order_user_rel',
        'order_id', 'transaction_id',
        string='Transaction Ids')