# -*- coding: utf-8 -*-
# from odoo import http


# class ExpPaletteTracking(http.Controller):
#     @http.route('/exp_palette_tracking/exp_palette_tracking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/exp_palette_tracking/exp_palette_tracking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('exp_palette_tracking.listing', {
#             'root': '/exp_palette_tracking/exp_palette_tracking',
#             'objects': http.request.env['exp_palette_tracking.exp_palette_tracking'].search([]),
#         })

#     @http.route('/exp_palette_tracking/exp_palette_tracking/objects/<model("exp_palette_tracking.exp_palette_tracking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('exp_palette_tracking.object', {
#             'object': obj
#         })
