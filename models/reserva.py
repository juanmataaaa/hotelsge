from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class Reserva(models.Model):
    _name = 'hotelsge.reserva'
    _description = 'Reserva de Hotel'

    name = fields.Char(string="Código de Reserva", compute="_compute_name", store=True)
    cliente_id = fields.Many2one('hotelsge.cliente', string="Cliente", required=True)
    fecha_entrada = fields.Date(string="Fecha de Entrada", required=True)
    fecha_salida = fields.Date(string="Fecha de Salida", required=True)
    habitaciones_ids = fields.Many2many('hotelsge.habitacion', string="Habitaciones")
    vehiculos = fields.Integer(string="Número de Vehículos", default=0)
    noches = fields.Integer(string="Noches", compute="_compute_noches", store=True)
    total = fields.Float(string="Total (€)", compute="_compute_total", store=True)

    @api.depends('fecha_entrada', 'fecha_salida')
    def _compute_noches(self):
        for r in self:
            if r.fecha_entrada and r.fecha_salida:
                r.noches = max((r.fecha_salida - r.fecha_entrada).days, 0)
            else:
                r.noches = 0

    @api.depends('habitaciones_ids', 'noches', 'vehiculos')
    def _compute_total(self):
        for r in self:
            precio_habitaciones = sum(h.precio_noche for h in r.habitaciones_ids)
            subtotal = precio_habitaciones * r.noches
            parking = r.vehiculos * 5 * r.noches
            descuento = 0.1 * subtotal if r.noches > 15 else 0
            r.total = subtotal + parking - descuento

    @api.depends('cliente_id', 'fecha_entrada')
    def _compute_name(self):
        for r in self:
            if r.cliente_id and r.fecha_entrada:
                r.name = f"{r.cliente_id.name} - {r.fecha_entrada}"
            else:
                r.name = ""

    @api.constrains('habitaciones_ids')
    def _check_habitaciones_unicas(self):
        for r in self:
            ids = [h.id for h in r.habitaciones_ids]
            if len(ids) != len(set(ids)):
                raise ValidationError("No se puede incluir la misma habitación más de una vez.")

    @api.constrains('fecha_entrada', 'fecha_salida')
    def _check_fechas(self):
        for r in self:
            hoy = fields.Date.today()
            if r.fecha_entrada < hoy:
                raise ValidationError("No se pueden hacer reservas con fecha anterior al día actual.")
            if r.fecha_entrada >= r.fecha_salida:
                raise ValidationError("La fecha de entrada debe ser anterior a la de salida.")

    @api.constrains('habitaciones_ids', 'fecha_entrada', 'fecha_salida')
    def _check_habitaciones_disponibles(self):
        for r in self:
            for habitacion in r.habitaciones_ids:
                reservas_solapadas = self.env['hotelsge.reserva'].search([
                    ('id', '!=', r.id),  # Excluir la reserva actual
                    ('habitaciones_ids', 'in', [habitacion.id]),
                    ('fecha_entrada', '<', r.fecha_salida),
                    ('fecha_salida', '>', r.fecha_entrada),
                ])
                if reservas_solapadas:
                    raise ValidationError(
                        f"La habitación {habitacion.name} ya está reservada en las fechas seleccionadas. "
                        f"Conflicto con la reserva {reservas_solapadas[0].name}"
                    )

    @api.constrains('vehiculos')
    def _check_max_vehiculos_reserva(self):
        for r in self:
            if r.vehiculos > 2:
                raise ValidationError("Solo puedes reservar hasta 2 vehículos por reserva.")

    @api.constrains('fecha_entrada', 'fecha_salida', 'vehiculos')
    def _check_plazas_semanales(self):
        for r in self:
            if not r.fecha_entrada or not r.fecha_salida:
                continue

        # Mantenemos el primer día de la semana (lunes)
        inicio = r.fecha_entrada
        fin = r.fecha_salida
        actual = inicio - timedelta(days=inicio.weekday())  # primer lunes anterior o igual

        while actual <= fin:
            semana_inicio = actual
            semana_fin = actual + timedelta(days=6)

            # Buscar reservas en la misma semana (menos la actual)
            reservas_semana = self.env['hotelsge.reserva'].search([
                ('id', '!=', r.id),
                ('fecha_entrada', '<=', semana_fin),
                ('fecha_salida', '>=', semana_inicio),
            ])

            total_vehiculos_semana = sum(res.vehiculos for res in reservas_semana) + r.vehiculos

            if total_vehiculos_semana > 8:
                raise ValidationError(
                    f"Hay un máximo de 8 vehículos por semana. "
                    f"Semana comenzando el {semana_inicio}: ya hay {total_vehiculos_semana - r.vehiculos} vehículos reservados."
                )

            actual += timedelta(days=7)

