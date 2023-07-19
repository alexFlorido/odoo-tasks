from odoo import fields, models 

class Course(models.Model):
    _name =  'course.course',
    _description = 'Course info'


    name = fields.Char(string="Title", required=True)
    active = fields.Boolean(string="Active", default=True)

    description = fields.Text()
    level = fields.Selection(string="Level",
                             selection=[
                                 ('beginner', "Beginner")
                                 ('intermediate', "Intermediate")
                                 ('advanced', "Advanced")
                             ],
                             copy=False)