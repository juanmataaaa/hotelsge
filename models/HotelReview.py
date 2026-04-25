from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HotelReview(models.Model):
    _name = 'hotelsge.review'
    _description = 'Valoración de Reserva de Hotel'

    cliente_id = fields.Many2one('hotelsge.cliente', string="Cliente", required=True)
    reserva_id = fields.Many2one('hotelsge.reserva', string="Reserva", required=True, domain="[('cliente_id', '=', cliente_id)]")
    estrellas = fields.Selection(
    [('1', '★☆☆☆☆'), ('2', '★★☆☆☆'), ('3', '★★★☆☆'), ('4', '★★★★☆'), ('5', '★★★★★')],
    string="Valoración (Estrellas)", required=True
)

    comentario = fields.Text(string="Comentario final", required=True)

    _sql_constraints = [
        ('review_unique', 'unique(cliente_id, reserva_id)', 'No puedes valorar dos veces la misma reserva.')
    ]

    @api.constrains('cliente_id', 'reserva_id')
    def _check_reserva_cliente(self):
        for rec in self:
            if rec.reserva_id.cliente_id.id != rec.cliente_id.id:
                raise ValidationError("Solo puedes valorar reservas realizadas por el cliente seleccionado.")
