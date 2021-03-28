# -*- coding: utf-8 -*-
from odoo import models, fields, api,_
from odoo.exceptions import AccessError, UserError, ValidationError
from datetime import datetime



class ExpPalette(models.Model):
    _name='exp.palette.tracking'
    ref = fields.Char(String="ref",required=True,copy=False,readonly=True,default=lambda self : _('New'))
    exp_picking_id = fields.Many2one('stock.picking')
    exp_partner_id = fields.Many2one('res.partner')
    exp_license_plate = fields.Char()
    exp_picking_partner_id = fields.Many2one('res.partner',compute='compute_picking')
    exp_picking_date_done = fields.Datetime(compute='compute_picking')
    exp_palette_count_plus = fields.Integer()
    exp_palette_count_minus = fields.Integer()
    exp_balance = fields.Integer(compute='compute_balance')

    @api.model
    def create(self,vals):
        if not vals.get('ref',False) or vals['ref'] == ('New'):
            vals['ref'] = self.env['ir.sequence'].next_by_code('exp.palette.tracking') or  _('New')
        res = super(ExpPalette,self).create(vals)
        return res

    def compute_balance(self):
        for record in self:
            record.exp_balance = record.exp_palette_count_plus -  record.exp_palette_count_minus

    @api.onchange('exp_picking_id')
    def compute_picking(self):
        for record in self:
            record.exp_picking_partner_id = record.exp_picking_id.partner_id
            record.exp_picking_date_done = record.exp_picking_id.date_done


class Parter(models.Model):
    _inherit='res.partner'
    exp_count =  fields.Integer(compute='compute_exp_palette')

    def compute_exp_palette(self):
        self.exp_count = self.env['exp.palette.tracking'].search_count([('exp_partner_id','=',self.id)])
        return {
            'type': 'ir.actions.act_window',
            'name': 'Exp palette',
            'view_mode': 'tree,form',
            'res_model': 'exp.palette.tracking',
            'domain': [('exp_partner_id', '=', self.id)],
            'context': "{'create': True}"
        }