# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real estate management"
    # _order = "sequence"

    name = fields.Char('Real Estate Name', required=True, translate=True)
    description = fields.Text('Description of the asset', required=True)
    postcode = fields.Char('ZIP code')
    date_availability = fields.Date('Date availability')
    expected_price = fields.Float('Expected price', required=True)
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Orientation',
        selection=[('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        help="Orientation is used to specify the garden orientation")
        