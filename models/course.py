# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api


class course(models.Model):
    _name = 'open_academy.course'
    _description = 'Modelo de curso'
    title = fields.Char(string='Nombre del curso')
    description = fields.Text(string='Breve descripcion del curso')
    user = fields.Many2one(comodel_name='res.users', string='Usario responsable')
    sessions = fields.One2many(comodel_name='open_academy.session', inverse_name='course', string='Sesiones')


    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('title', '=like', u"Copy of {}%".format(self.title))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.title)
        else:
            new_name = u"Copy of {} ({})".format(self.title, copied_count)

        default['title'] = new_name
        return super(course, self).copy(default)

    _sql_constraints = [
    ('title_description_check',
    'CHECK(title != description)',
    'La descripcion del curso no debe ser la mismo que el nombre'),
   ('title_unique',
         'UNIQUE(title)',
         'El nombre del curso debe ser Unico'),
    ]
