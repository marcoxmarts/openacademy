# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Partner(models.Model):
	_inherit = 'res.partner'

	instructor = fields.Boolean('Instructor asignado', default=False)
	session_ids = fields.Many2many('openacademy.session', string="Sessiones atentidas", readonly=True)

