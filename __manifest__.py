{
    'name': "Odoo Academy",
    'summary': """Module to Logistic Handle of Course and Sessions""",
    'description': """Module Handle: 
            - Curses
            - Sessions
            - Attendees
            """,
    'license': "OPL-1",
    'author': "alexFlorido",
    'website': 'www.odoo.com',
    'category': "Custom Modules/Tech Trainning",
    "depends": ['sale'] ,
    'data': [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        'data/session_data.xml',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sales_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml'

    ],
    'demo': [
        "demo/course_demo.xml"
    ],
    'application': True,
}