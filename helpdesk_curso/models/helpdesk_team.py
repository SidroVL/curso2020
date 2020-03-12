# Copyright 2015-12/03/20 Alia Technologies, S.L. - http://www.alialabs.com 
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class HelpdeskTeam(models.Model):
    _name = 'helpdesk.team'
    _description = 'Team'

    name = fields.Char(string="Name", required=True)
    ticket_ids = fields.One2many(comodel_name='helpdesk.ticket', inverse_name="team_id", string="Tickets")
    helpdesk_ticket_ids = fields.Many2many(comodel_name='helpdesk.ticket', string="Team Tickets")
    user_ids = fields.One2many(comodel_name='res.users', inverse_name='helpdesk_team_id', string='Users')

