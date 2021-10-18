
# -*- coding: utf-8 -*-
from odoo import api, fields, models, exceptions
from datetime import timedelta

class session(models.Model):
    _name = 'open_academy.session'
    _description = 'Un nuevo modelo para la sesiones de un curso'

    name = fields.Char(string='Nombre')
    start_date = fields.Date(string='Fecha de inicio')
    duration = fields.Float(string='Duracion de la sesion')
    seats = fields.Integer(string='Numero de asientos')
    instructor = fields.Many2one(comodel_name='res.partner', string='Instructor',domain="['|',('instructor','=','True'),'|',('teacher1','=','True'),('teacher2','=','True')]")
    course = fields.Many2one(comodel_name='open_academy.course', string='Curso')
    attendes = fields.Many2many(comodel_name='res.partner', string='Asistentes')
    taken_seats = fields.Float(string='Porcentaje de asientos tomados', compute='_taken_seats')
    active = fields.Boolean(default=True)
    color = fields.Integer()
    end_date = fields.Date(string="Fecha de cierre", store=True,compute='_get_end_date', inverse='_set_end_date')
    attendees_count = fields.Integer( string="Numero de asistentes", compute='_get_attendees_count', store=True)


    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            start = fields.Datetime.from_string(r.start_date)
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = start + duration


    @api.depends('attendes')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendes)
    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue
            start_date = fields.Datetime.from_string(r.start_date)
            end_date = fields.Datetime.from_string(r.end_date)
            r.duration = (end_date - start_date).days + 1

    @api.depends('seats','attendes')
    def _taken_seats(self):
        for record in self:
            if not record.seats:
                record.taken_seats=0.0
            else:
                record.taken_seats = (100/record.seats)*len(record.attendes)

    @api.onchange('seats', 'attendes')
    def _verify_valid_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Valor incorrecto para asientos",
                    'message': "El numero de asientos disponibles no debe ser negativo",
                },
            }
        if self.seats < len(self.attendes):
            return {
                'warning': {
                    'title': "Muchos asistentes",
                    'message': "Aumenta los asientos o reduce los asistentes",
                },
            }

    @api.constrains('instructor', 'attendes')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor and r.instructor in r.attendes:
                raise exceptions.ValidationError("Un instructor no puede ser un asistente")
    
    
        
