from odoo import models, fields

class Cliente(models.Model):
    _name = 'hotelsge.cliente'
    _description = 'Cliente del Hotel'

    name = fields.Char(string="Nombre", required=True)
    email = fields.Char(string="Email", required=True)
    telefono = fields.Char(string="Teléfono", required=True)
    reserva_ids = fields.One2many(
    'hotelsge.reserva',    
    'cliente_id',           
    string="Reservas"
)


    _sql_constraints = [
        ('unique_email', 'unique(email)', 'El correo electrónico debe ser único.')
    ]
