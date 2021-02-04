from odoo import models, fields


class AgentUser(models.Model):
    _inherit = 'res.users'

    remote_agent = fields.One2many('remote_agent.agent', inverse_name='user')

