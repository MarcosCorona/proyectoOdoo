from odoo import models, fields, api

class tienda(models.Model):
    _nombre = 'tiendas.tienda'
    _descripcion = 'Define los datos de cada tienda.' 

    #atributos
    idTienda = fields.Integer(string='Id ', required=True)
    nombreTienda = fields.Char(string='Nombre tienda ',required=True)
    direccionTienda = fields.Char(string='Direccion tienda ',required=True)

class trabajador(models.Model):
    _name = 'tiendas.trabajador'
    _descripcion = 'Atributos de trabajador por tienda.'

    #Atributos
    
    dniTrabajador = fields.Char(string='DNI',required=True)
    nombreTrabajador = fields.Char(string='Nombre',required=True)
    correoTrabajador = fields.Char(string='Correo',required=True)
    fechaNacimiento = fields.Date(string='Fecha nacimiento', required=True, default = fields.date.today())





    