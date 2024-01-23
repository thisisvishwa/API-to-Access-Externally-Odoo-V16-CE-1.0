from odoo import api, fields, models

class ApiConfigWizard(models.TransientModel):
    _name = 'api.config.wizard'
    _description = 'API Configuration Wizard'

    api_global_config = fields.Many2one('api.global.config', string='Global Configuration')
    enable_endpoints = fields.Boolean(string='Enable Endpoints')
    disable_endpoints = fields.Boolean(string='Disable Endpoints')
    endpoint_ids = fields.Many2many('api.endpoint', string='API Endpoints')
    display_format = fields.Selection([
        ('swagger', 'Swagger'),
        ('openapi', 'OpenAPI')
    ], string='Display Format', default='swagger')

    @api.model
    def default_get(self, fields):
        res = super(ApiConfigWizard, self).default_get(fields)
        config = self.env['api.global.config'].search([], limit=1)
        if config:
            res.update({
                'api_global_config': config.id,
                'enable_endpoints': config.enable_endpoints,
                'disable_endpoints': config.disable_endpoints,
                'endpoint_ids': [(6, 0, config.endpoint_ids.ids)],
                'display_format': config.display_format,
            })
        return res

    def apply_configuration(self):
        self.ensure_one()
        config = self.api_global_config
        config.enable_endpoints = self.enable_endpoints
        config.disable_endpoints = self.disable_endpoints
        config.endpoint_ids = [(6, 0, self.endpoint_ids.ids)]
        config.display_format = self.display_format
        return {'type': 'ir.actions.act_window_close'}