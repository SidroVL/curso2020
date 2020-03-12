# Copyright 2015-12/03/20 Alia Technologies, S.L. - http://www.alialabs.com 
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    ticket_ids = fields.Many2many(string='Tickets',
                                  relation='helpdesk_tickets_user_rel',
                                  column1='user_id',
                                  column2='helpdesk_id',
                                  comodel_name='helpdesk.ticket',
                                  )

    helpdesk_code = fields.Char(string="Helpdesk Code")
    helpdesk_team_id = fields.Many2one(comodel_name='helpdesk.team', string='Team')
