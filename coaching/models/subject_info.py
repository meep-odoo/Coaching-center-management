from odoo import fields, models


class subjectModel(models.Model):
    _name = "subject.info"
    _description = "Subject Model"

    subject_name = fields.Char(required=True)
    subject_code   = fields.Integer(required=True)
    subject_difficulty = fields.Selection(
        [('easy', 'Easy'),
         ('intermediate', 'Intermediate'),
         ('advanced', 'Advanced')],
        string='Difficulty',
        default = "",
        required=True,
        copy=False)

    _sql_constraints = [
        ('unique_subject_code', 'UNIQUE(subject_code)', 'Subject Code must be unique.'),
    ]
