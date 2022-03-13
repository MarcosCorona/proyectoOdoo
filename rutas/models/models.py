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

class repartidor(models.Model):
    _name = 'rutas.repartidor'
    _description = 'Repartidores disponibles.'

    #atributos
    dniTrabajador = fields.Char(string='DNI',required=True)
    nombreTrabajador = fields.Char(string='Nombre',required=True)
    correoTrabajador = fields.Char(string='Correo',required=True)
    fechaNacimiento = fields.Date(string='Fecha nacimiento', required=True, default = fields.date.today())
    edad = fields.Integer('Edad', compute='_getEdad')   
    #relaccion
  
    #validacion
