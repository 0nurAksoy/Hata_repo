# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    project_choose_id = fields.Many2one(comodel_name="project.project", string="Proje")
    task_choose_id = fields.Many2one(comodel_name="project.task",  string="Görev",
                       domain="[('project_id', '=', project_id)]")
