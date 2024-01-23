{
    'name': 'Odoo External API Access',
    'version': '1.0',
    'summary': 'API Documentation and Interactive Exploration Module',
    'sequence': 10,
    'author': 'Vishwa G',
    'website': 'https://thisis.com',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'web'],
    'external_dependencies': {'python': []},
    'data': [
        'security/ir.model.access.csv',
        'views/api_access_views.xml',
        'views/templates.xml',
        'data/api_data.xml',
        'demo/api_demo.xml',
    ],
    'demo': [
        'demo/api_demo.xml',
    ],
    'qweb': [
        'static/src/xml/api_templates.xml',
    ],
    'js': [
        'static/src/js/api_interactive.js',
    ],
    'css': [
        'static/src/css/api_styles.css',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
Odoo External API Access Module
================================

This module provides dynamic API documentation, interactive exploration, and execution of API operations directly within the Odoo backend interface.
    """,
}