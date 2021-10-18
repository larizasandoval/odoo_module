# -*- coding: utf-8 -*-

from odoo import api, fields, models


class partner(models.Model):
    _inherit='res.partner'

    instructor = fields.Boolean(string='Es instructor?')
    teacher1 = fields.Boolean(string='Es profesor nivel 1?')
    teacher2 = fields.Boolean(string='Es profesor nivel 2?')
    sessions = fields.Many2many(comodel_name='open_academy.session', string='Sesiones')
    
    
