# -*- coding: utf-8 -*-
# from odoo import http


# class EleroxModule(http.Controller):
#     @http.route('/elerox_module/elerox_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/elerox_module/elerox_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('elerox_module.listing', {
#             'root': '/elerox_module/elerox_module',
#             'objects': http.request.env['elerox_module.elerox_module'].search([]),
#         })

#     @http.route('/elerox_module/elerox_module/objects/<model("elerox_module.elerox_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('elerox_module.object', {
#             'object': obj
#         })

