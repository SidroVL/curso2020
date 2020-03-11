# Copyright 2015-11/03/20 Alia Technologies, S.L. - http://www.alialabs.com 
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class HelpdeskTicket(models.Model):

    _name = 'helpdesk.ticket'

    name = fields.Char(string="Name", required=True)
    description = fields.Text('Description')
    date_deadline = fields.Datetime('Date limit')
