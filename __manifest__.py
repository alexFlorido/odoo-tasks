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
    "depends": ['base'] ,
    'data': [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
    ],
    'demo': [
        "demo/course_demo.xml"
    ],
    'application': True,
}