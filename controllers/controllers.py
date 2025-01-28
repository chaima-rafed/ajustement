# -*- coding: utf-8 -*-
# from odoo import http


# class Ajustements(http.Controller):
#     @http.route('/ajustements/ajustements', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ajustements/ajustements/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ajustements.listing', {
#             'root': '/ajustements/ajustements',
#             'objects': http.request.env['ajustements.ajustements'].search([]),
#         })

#     @http.route('/ajustements/ajustements/objects/<model("ajustements.ajustements"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ajustements.object', {
#             'object': obj
#         })

