# Copyright 2015-11/03/20 Alia Technologies, S.L. - http://www.alialabs.com 
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class HelpdeskTicket(models.Model):

    _name = 'helpdesk.ticket'
    _descriotion = 'Ticket'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string='Description')
    date_deadline = fields.Datetime(string='Date limit')
    team_id = fields.Many2one(string="Team", comodel_name='helpdesk.team')
    stage_id = fields.Many2one(string="Stage", comodel_name='helpdesk.ticket.stage')
    user_ids = fields.Many2many(string="Users",
                                relation='helpdesk_tickets_user_rel',
                                column1='helpdesk_id',
                                column2='user_id',
                                comodel_name='res.users')
    responsible_id = fields.Many2one(string='Responsible', comodel_name='res.users')

    @api.onchange('team_id')
    def _onchange_team_id(self):
        for ticket in self:
            team = self.env['helpdesk.team'].browse(ticket.team_id.id)
            team = self.env['helpdesk.team'].search([('id', '=', ticket.team_id.id)])
            if team:
                for user in team.user_ids:
                    ticket.user_ids = [(4, user.id)]

    def assign_to_me(self):
        for ticket in self:
            user_id = self.env.user.id
            if user_id:
                ticket.user_ids = [[6, False, [user_id]]]

    def set_responsible(self):
        for ticket in self:
            user_id = self.env.user
            if user_id:
                ticket.responsible_id = user_id

