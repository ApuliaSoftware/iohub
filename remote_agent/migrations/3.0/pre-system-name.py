import logging
from odoo import api, SUPERUSER_ID

logger = logging.getLogger(__name__)


def migrate(cr, version):
    try:
        with api.Environment.manage():
            env = api.Environment(cr, SUPERUSER_ID, {})
            env.cr.execute(
                'ALTER TABLE remote_agent_agent ADD COLUMN '
                'system_name VARCHAR')
            env.cr.execute(
                'UPDATE remote_agent_agent SET system_name = agent_uid')
            env.cr.commit()
    except:
        logger.exception('Remote Agent 3.0 migration error:')
