from odoo import models, fields

class Habitacion(models.Model):
    _name = 'hotelsge.habitacion'
    _description = 'Habitación del Hotel'

    name = fields.Char(string="Identificador", required=True)
    tipo = fields.Selection([
        ('simple', 'Simple'),
        ('doble', 'Doble'),
        ('suite', 'Suite')
    ], string="Tipo", required=True)
    estado = fields.Selection([
        ('libre', 'Libre'),
        ('ocupada', 'Ocupada')
    ], string="Estado", default='libre', required=True)
    precio_noche = fields.Float(string="Precio por Noche", required=True)

    _sql_constraints = [
        ('unique_identificador', 'unique(name)', 'El identificador de la habitación debe ser único.'),
        ('positive_precio', 'CHECK(precio_noche >= 0)', 'El precio debe ser mayor o igual a 0.')
    ]
def action_actualizar_estado(self):
        hoy = fields.Date.today()
        for habitacion in self:
           
            reservas_activas = self.env['hotelsge.reserva'].search([
                ('habitaciones_ids', 'in', [habitacion.id]),
                ('fecha_entrada', '<=', hoy),
                ('fecha_salida', '>=', hoy),
            ])
            
            if reservas_activas:
                habitacion.estado = 'ocupada'
            else:
                habitacion.estado = 'libre'