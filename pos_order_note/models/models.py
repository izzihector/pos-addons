from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"
    pos_notes = fields.Text("Notes for POS", translate=True)


class PosProductNotes(models.Model):
    _name = "pos.product_notes"
    _description = "POS Product Notes"

    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string="Note")
