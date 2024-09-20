# -*- coding: utf-8 -*-
##########################################################################
#
#    Copyright (c) 2017-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#
##########################################################################

from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError

class IncidentType(models.Model):
    _name = "incident.type"
    _description = "Incident Type"

    name = fields.Char(string="Name", required=True)

class TeamIncident(models.Model):
    _name = 'team.incident'
    _inherit = ['mail.thread']
    _description = "Team Incidents"

    @api.onchange('team_id')
    def onchange_team_id(self):
        res = self.get_involved_user()
        return {"domain":{'involved_user_id':[('id', 'in', res)]}}

    @api.model
    def get_involved_user(self):
        user_ids = []
        if self.team_id:
            user_ids.append(self.team_id.manager.id)
            user_ids += self.team_id.members.ids
        return user_ids

    def reason_wizard_action(self):
        leader_group = self.env.ref('project_advance_team.group_project_leader').id
        if self.create_uid == self.env.user or leader_group in self.env.user.groups_id.ids:
            return {
            'name': 'Reason',
            'res_model': 'reason.wizard',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'target': 'new',
            'view_id': self.env.ref('incident_management.reason_wizard').id
            }
        else:
            raise UserError(_('Sorry, you cannot cancel this incident.'))

    name = fields.Char(string="Incident Title", required=True)
    description = fields.Text(string="Description", tracking=True)
    involved_user_id = fields.Many2one("res.users", string='Person Involved', required=True,tracking=True, domain=lambda self: [('id', 'in', self.get_involved_user())])
    team_id = fields.Many2one('wk.team', 'Team', required=True, tracking=True)
    incident_type = fields.Many2one('incident.type', string=" Type of incident", required=True, tracking=True)
    incident_date = fields.Datetime(string="Date of incident", required=True, default=fields.Datetime.now(), tracking=True)
    attention_type = fields.Selection([('involved', 'Was Involved'),('reported', 'Reported to me')], string='How did the incident come to your attention?', default='involved')
    state = fields.Selection([('open', 'Open'), ('cancelled', 'Cancelled'), ('resolved', 'Resolved')], string="State", default='open', tracking=True)

class WkTeam(models.Model):
    _inherit = 'wk.team'

    incident_ids = fields.One2many('team.incident', 'team_id', string='Incidents')
    incident_count = fields.Integer(compute='get_count', compute_sudo=True)

    def get_count(self):
        for obj in self:
            obj.incident_count = len(obj.incident_ids)
