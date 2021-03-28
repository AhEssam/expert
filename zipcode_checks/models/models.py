# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    auth_id = fields.Char(string='Authentication id')
    token_id = fields.Char(string='Token id')

    # @api.model
    # def get_values(self):
    #     res = super(ResConfigSettings, self).get_values()
    #     print('<>>>>>>>>>>>>>>>>>>>',self.auth_id)
    #
    #     res.update(
    #         auth_id=self.auth_id,
    #         token_id=self.token_id,
    #     )
    #     return res

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            auth_id = self.env['ir.config_parameter'].sudo().get_param('zipcode_checks.auth_id'),
            token_id = self.env['ir.config_parameter'].sudo().get_param('zipcode_checks.token_id'),
        )
        return res

    # @api.multi
    def set_values(self):
        for record in self:
            super(ResConfigSettings, self).set_values()
            param = self.env['ir.config_parameter'].sudo()

            auth_id = record.auth_id and record.auth_id or False
            token_id = record.token_id and record.token_id or False

            param.set_param('zipcode_checks.auth_id', auth_id)
            param.set_param('zipcode_checks.token_id', token_id)

