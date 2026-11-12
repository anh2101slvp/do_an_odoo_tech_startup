from odoo import models, fields

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    main_tech_stack = fields.Selection([
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('fullstack', 'Fullstack'),
        ('devops', 'DevOps')
    ], string='Mảng công nghệ chính')
    
    seniority_level = fields.Selection([
        ('intern', 'Intern'),
        ('fresher', 'Fresher'),
        ('junior', 'Junior'),
        ('mid', 'Mid-level'),
        ('senior', 'Senior')
    ], string='Cấp độ chuyên môn')
    
    github_profile = fields.Char(string='Link GitHub')