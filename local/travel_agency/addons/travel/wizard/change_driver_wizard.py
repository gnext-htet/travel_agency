from odoo import api, fields, models,_
from odoo.exceptions import UserError

class ChangeDriverWizard(models.TransientModel):
    _name = 'change.driver.wizard'
    _description = 'Change Driver Wizard'

    partner_id = fields.Many2one('res.partner', string="Partner", required=True)
    join_date = fields.Date(string="Join Date", default=lambda self: fields.Date.today(), required=True)

    def change_driver(self):
        # Retrieve context
        context = self.env.context
        active_model = context.get('active_model')
        active_id = context.get('active_id')
        travel_car_id = self.env[active_model].browse(active_id)

        if self.partner_id == travel_car_id.partner_id:
            raise UserError(_("Change Driver should not the same."))

        values = {
            "travel_car_id": travel_car_id.id,
            "driver_id": travel_car_id.partner_id.id,
            "join_date": travel_car_id.join_date,
            "fired_date": fields.Date.today(),
        }
        self.env['travel.driver.history'].create(values)
        # Update the travel car record with the new driver
        travel_car_id.partner_id = self.partner_id
        travel_car_id.join_date = self.join_date


