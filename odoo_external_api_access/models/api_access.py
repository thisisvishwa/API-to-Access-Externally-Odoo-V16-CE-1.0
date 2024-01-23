from odoo import models, fields, api

class ApiAccess(models.Model):
    _name = 'api.access'
    _description = 'API Access Configuration'

    name = fields.Char(string='Name', required=True)
    endpoint = fields.Char(string='Endpoint', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    request_method = fields.Selection([
        ('get', 'GET'),
        ('post', 'POST'),
        ('put', 'PUT'),
        ('delete', 'DELETE')
    ], string='Request Method', required=True)
    request_parameters = fields.One2many('api.parameter', 'api_access_id', string='Request Parameters')
    response_structure = fields.Text(string='Response Structure')
    security_role_ids = fields.Many2many('res.groups', string='Security Roles')

    @api.model
    def create(self, vals):
        # Custom logic before creating a new API Access record
        return super(ApiAccess, self).create(vals)

    def write(self, vals):
        # Custom logic before writing to an existing API Access record
        return super(ApiAccess, self).write(vals)

    def unlink(self):
        # Custom logic before deleting an API Access record
        return super(ApiAccess, self).unlink()

    def toggle_active(self):
        for record in self:
            record.active = not record.active

class ApiParameter(models.Model):
    _name = 'api.parameter'
    _description = 'API Request Parameters'

    name = fields.Char(string='Parameter Name', required=True)
    parameter_type = fields.Selection([
        ('string', 'String'),
        ('integer', 'Integer'),
        ('float', 'Float'),
        ('boolean', 'Boolean'),
        ('file', 'File')
    ], string='Parameter Type', required=True)
    required = fields.Boolean(string='Required')
    default_value = fields.Char(string='Default Value')
    description = fields.Text(string='Description')
    api_access_id = fields.Many2one('api.access', string='API Access', ondelete='cascade')