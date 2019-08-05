# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Assign/Unassign Followers',

    'version': '12.0.0.0.0',

    'summary': 'Assign and Unassign Followers',

    'author': 'FOSS INFOTECH PVT LTD, Odoo Community Association (OCA)',

    'license': 'AGPL-3',

    'sequence': 10,

    'website': 'http://www.fossinfotech.com',

    'category': 'Tools',

    'website': 'https://www.fossinfotech.com/',

    'data': [
        'views/assign_followers_view.xml',
        'security/ir.model.access.csv'
    ],

    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
        'static/description/index.html'
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
