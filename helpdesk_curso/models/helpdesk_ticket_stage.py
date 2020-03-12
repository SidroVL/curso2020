# Copyright 2015-12/03/20 Alia Technologies, S.L. - http://www.alialabs.com 
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class HelpdeskTicketStage(models.Model):
    _name = 'helpdesk.ticket.stage'
    _description = 'Ticket Stage'

    name = fields.Char(string="Name", required=True)
    ticket_id = fields.One2many(comodel_name='helpdesk.ticket', inverse_name='stage_id', string="Ticket")

