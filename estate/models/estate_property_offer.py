from odoo import api, fields, models
from datetime import timedelta


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Real Estate Property Offer"
    # _order = "sequence"

    price = fields.Float('Price')
    status = fields.Selection([
        ('accepted', 'Accepted'),
        ('refused', 'Refused')
    ], string='Status', copy=False)
    partner_id = fields.Many2one('res.partner', string='Partner', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)
    validity = fields.Integer(string="Validity", default=7)
    date_deadline = fields.Date(string="Deadline (days)", compute="_compute_date_deadline")

    @api.depends('validity')
    def _compute_date_deadline(self):
        for record in self:
            if record.validity:
                if self.create_date:
                    record.date_deadline = self.create_date + timedelta(days=record.validity)
                else:
                    record.date_deadline = fields.Datetime.today() + timedelta(days=record.validity)
            else:
                record.date_deadline = None