from odoo import fields, models, api
from odoo.exceptions import UserError


class coachingModel(models.Model):
    _name = "student.info"
    _description = "Student Model"

    student_name = fields.Char(required=True)
    student_roll_no   = fields.Integer(required=True)
    phone_no = fields.Char()
    class_ = fields.Integer(required=True,default='6')


    _sql_constraints = [
        ('unique_student_roll_no', 'UNIQUE(student_roll_no)', 'Student Roll No. must be unique.'),
    ]

    @api.constrains('class_')
    def _check_valid_class_range(self):
        for record in self:
            if record.class_ and (record.class_ < 6 or record.class_ > 10):
                raise UserError("Class must be in the range of 6 to 10.")

    @api.constrains('phone_no')
    def _check_valid_phone_no(self):
        for record in self:
            if record.phone_no and len(record.phone_no) != 10:
                raise UserError("Phone number must be a 10-digit numeric value.")
