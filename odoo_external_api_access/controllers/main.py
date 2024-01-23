from odoo import http
from odoo.http import request

class OdooExternalAPIAccessController(http.Controller):

    @http.route('/api/documentation', auth='user', type='http', website=True)
    def api_documentation(self, **kw):
        # Ensure the user has the right permissions
        if not request.env.user.has_group('odoo_external_api_access.api_user_permissions'):
            return request.render('odoo_external_api_access.api_access_denied')

        # Retrieve API documentation data
        api_endpoints = request.env['api_access'].search([])
        values = {
            'api_endpoints': api_endpoints,
            'api_documentation_url': API_DOCUMENTATION_URL,
        }
        return request.render('odoo_external_api_access.api_documentation_template', values)

    @http.route('/api/execute', auth='user', type='json', methods=['POST'], website=True)
    def execute_api(self, endpoint_id, params):
        # Ensure the user has the right permissions
        if not request.env.user.has_group('odoo_external_api_access.api_user_permissions'):
            return {'error': API_ACCESS_DENIED}

        # Find the endpoint object
        endpoint = request.env['api_access'].browse(endpoint_id)
        if not endpoint:
            return {'error': API_ENDPOINT_DISABLED}

        # Execute the API operation
        try:
            response = endpoint.execute_operation(params)
            # Update API history
            request.env['api_history'].sudo().create({
                'user_id': request.env.user.id,
                'endpoint_id': endpoint.id,
                'parameters': params,
                'response': response,
            })
            return {'success': API_EXECUTION_SUCCESS, 'response': response}
        except Exception as e:
            return {'error': API_EXECUTION_FAILURE, 'message': str(e)}

    @http.route('/api/explore', auth='user', type='http', website=True)
    def explore_api(self, endpoint_id):
        # Ensure the user has the right permissions
        if not request.env.user.has_group('odoo_external_api_access.api_user_permissions'):
            return request.render('odoo_external_api_access.api_access_denied')

        # Find the endpoint object
        endpoint = request.env['api_access'].browse(endpoint_id)
        if not endpoint:
            return request.render('odoo_external_api_access.api_endpoint_disabled')

        values = {
            'endpoint': endpoint,
            'api_request_parameters': endpoint.get_request_parameters(),
            'api_response_structure': endpoint.get_response_structure(),
        }
        return request.render('odoo_external_api_access.api_explore_template', values)