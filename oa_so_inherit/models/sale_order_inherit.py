# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    project_id = fields.Many2one(comodel_name="project.project")
    task_id = fields.Many2one(comodel_name="project.task")
