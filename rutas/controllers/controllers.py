# -*- coding: utf-8 -*-
# from odoo import http


<<<<<<< HEAD
# class Rutas(http.Controller):
#     @http.route('/rutas/rutas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rutas/rutas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rutas.listing', {
#             'root': '/rutas/rutas',
#             'objects': http.request.env['rutas.rutas'].search([]),
#         })

#     @http.route('/rutas/rutas/objects/<model("rutas.rutas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rutas.object', {
=======
# class Tiendas(http.Controller):
#     @http.route('/tiendas/tiendas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tiendas/tiendas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tiendas.listing', {
#             'root': '/tiendas/tiendas',
#             'objects': http.request.env['tiendas.tiendas'].search([]),
#         })

#     @http.route('/tiendas/tiendas/objects/<model("tiendas.tiendas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tiendas.object', {
>>>>>>> 32f68800703ac4294af370149e9c76497b2b20d4
#             'object': obj
#         })
