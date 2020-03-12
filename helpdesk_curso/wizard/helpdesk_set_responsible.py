# Copyright 2015-12/03/20 Alia Technologies, S.L. - http://www.alialabs.com 
# @author:alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api, _


class HelpdeskSetResponsible(models.TransientModel):
    _name = 'helpdesk.set.responsible'
    _description = 'Set Ticket Responsible'

    tickets_qty = fields.Integer(string="Tickets Qty")
    ticket_ids = fields.Many2many(string="User Tickets", comodel_name='helpdesk.ticket')

    @api.model
    def default_get(self, fields):
        res = super(HelpdeskSetResponsible, self).default_get(fields)
        user_id = self.env.uid
        tickets = self.env['helpdesk.ticket'].search([('responsible_id', '=', user_id)])
        if tickets:
            qty = len(tickets)
            res['tickets_qty'] = qty
            ticket_ids = []
            for ticket in tickets:
                ticket_ids.append(ticket.id)
            res['ticket_ids'] = [[6, False, ticket_ids]]

        return res

    def set_responsible(self):
        active_ids = self._context.get('active_ids', [])
        active_model = self._context.get('active_model', [])
        if active_ids and active_model and active_model == 'helpdesk.ticket':
            tickets = self.env['helpdesk.ticket'].browse(active_ids)
            for ticket in tickets:
                user_id = self.env.user
                if user_id:
                    ticket.responsible_id = user_id
