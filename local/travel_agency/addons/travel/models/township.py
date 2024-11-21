from odoo import api, fields, models

class Township(models.Model):
    _name = 'travel.township'
    _description = 'Township'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(track_visibility='onchange')
    gate_ids = fields.One2many('travel.gate', 'township_id')


