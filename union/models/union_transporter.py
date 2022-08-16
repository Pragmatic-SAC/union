# -*- coding: utf-8 -*-
"""
Autor: Kelvin Meza
Website: https://kelvinthony.github.io/
"""

from odoo import api, fields, models


class UnionTransporter(models.Model):
    _name = 'union.transporter'
    _description = 'Union Transporter'

    name = fields.Char('Transporter')
    active = fields.Boolean('Active')
