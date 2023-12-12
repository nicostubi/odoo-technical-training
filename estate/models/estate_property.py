# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models
from datetime import timedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real estate management"
    # _order = "sequence"

    name = fields.Char('Real Estate Name', default="Unknown", required=True, translate=True)
    description = fields.Text('Description of the asset', required=True)
    postcode = fields.Char('ZIP code')
    date_availability = fields.Date('Date availability', default=fields.Datetime.today()+timedelta(days=90), copy=False)
    expected_price = fields.Float('Expected price', required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()   
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Orientation is used to specify the garden orientation")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('offer_received', 'Offer Received'), ('offer_accepted', 'Offer Accepted'), ('sold', 'Sold'), ('canceled', 'Canceled')],
        required=True, copy=False, default="new")
    property_type_id = fields.Many2one('estate.property.type', string="Property Type")
    #user_id = fields.Many2one('res.users', string='Salesman', index=True, tracking=True, default=lambda self: self.env.user)

        