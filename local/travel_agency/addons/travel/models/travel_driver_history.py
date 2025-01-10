from odoo import api, fields, models ,_
from odoo.exceptions import UserError, ValidationError



class TravelDriverHistory(models.Model):
    _name = 'travel.driver.history'
    _description = 'TravelDriverHistory'

    #relation
    travel_car_id = fields.Many2one('travel.car')
    travel_agency_id = fields.Many2one('travel.agency', related='travel_car_id.travel_agency_id')
    driver_id = fields.Many2one('res.partner')
    
    join_date = fields.Date()
    fired_date = fields.Date()
    
    #check join_date and fired_date
    @api.constrains('join_date', 'fired_date')
    def _check_join_fired_date(self):
        if self.join_date > self.fired_date:
            raise UserError(_("Join Date should be greater than Fired Date"))
    
    

    
