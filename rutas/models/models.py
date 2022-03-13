<<<<<<< HEAD
# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class rutas(models.Model):
#     _name = 'rutas.rutas'
#     _description = 'rutas.rutas'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

import string
from odoo import models, fields, api, exceptions
from datetime import date
from dateutil.relativedelta import *

class ruta(models.Model):
    _name = 'rutas.ruta'
    _description = 'Coleccion de rutas.' 

    #atributos
    idRuta = fields.Integer(string='Id ', required=True)
    dirSalida = fields.Char(string='Comienzo ruta:  ',required=True)
    dirEntrega = fields.Char(string='Fin ruta: ',required=True)
    tipoViaje = fields.Selection(string='Tipo viaje', selection=[('Viaje corto'), ('Viaje medio'),('Viaje largo.')])
    #relaccion 
    camion_id = fields.Many2many('rutas.camion',string='Camiones:')

class camion(models.Model):
    _name = 'rutas.camion'
    _description = 'Camion disponibles.'

    #atributos
    idCamion = fields.Char(string='ID:',required=True)
    numBastidor = fields.Char(string='Nº bastidor',required=True)
    matricula = fields.Char(string='Matricula',required=True)
    #relaccion
    ruta_ids = fields.Many2many('rutas.camion',string='Rutas:')
    trabajador_id = fields.Many2one('tiendas.trabajador',String="Trabajadores:")
    #validacion

