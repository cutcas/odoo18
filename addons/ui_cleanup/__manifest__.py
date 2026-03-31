# -*- coding: utf-8 -*-
{
    'name': 'UI Cleanup',
    'version': '18.0.1.0.0',
    'sequence': 1,
    'category': 'Tools',
    'summary': 'Clean Odoo interface by hiding branding and unnecessary menus',
    'description': """
        UI Cleanup
        ===================
        
        This module provides a cleaner, more professional Odoo interface by:
        
        * Hiding "Powered by Odoo" branding from the login screen
        * Removing unnecessary items from the user menu (top right corner):
            - Documentation
            - Support
            - Shortcuts
            - Odoo.com account
            - Install PWA
            - Tour onboarding
        
        This creates a streamlined, focused user experience for ERP.
    """,
    'author': 'Intersel',
    'website': 'https://intertel.mx/',
    'license': 'LGPL-3',
    'images': ['static/description/icon.svg'],
    'depends': [
        'base',
        'web'
    ],
    'data': [
        'views/login_templates.xml'
    ],
    'assets': {
        'web.assets_backend': [
            'ui_cleanup/static/src/js/user_menus.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
