from odoo import api, fields, models, _
from odoo.exceptions import UserError
class TravelAgency(models.Model):
    _name = 'travel.agency'
    _description = 'TravelAgency'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(track_visibility='onchange')
    reference = fields.Char(track_visibility='onchange', default=lambda self:_('New'), copy=False)
    license_no = fields.Char(track_visibility='onchange')
    travel_car_ids = fields.One2many('travel.car','travel_agency_id')

    _sql_constraints = [
        ('license_no_uniq', 'unique (license_no)', 'license Number must be unique.')
    ]

    @api.model
    def create(self, values):
        if values.get('reference', _('New')) == _('New'):
            values['reference'] = self.env['ir.sequence'].next_by_code('travel.agency') or _('New')

        return super(TravelAgency, self).create(values)


    @api.constrains('name')
    def _check_python_code(self):
        for record in self:
            domain = [('name', '=', record.name), ('id', '!=', record.id)]
            if self.search(domain):
                raise UserError(_("Agency Name already exists."))