# -*- coding: utf-8 -*-

from odoo import models, fields, api

class wizard(models.TransientModel):
    _name = 'open_academy.wizard'

    def _default_session(self):
        return self.env['open_academy.session'].browse(self._context.get('active_ids'))

    session_ids = fields.Many2one('open_academy.session', string="Sesiones", required=True)#,default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string="Asistentes")

    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}
