from odoo import api, fields, models 

class TravelDriverHistory(models.Model):
    _name = 'travel.driver.history'
    _description = 'TravelDriverHistory'

    travel_car_id = fields.Many2one('travel.car')
    driver_id = fields.Many2one('res.partner')
    join_date = fields.Date()
    fired_date = fields.Date()

    
