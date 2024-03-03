{
    'name': "coaching",
    'version': '1.0',
    'depends': ['base'],
    'data':[ 'security/ir.model.access.csv',
             'view/student_info_views.xml',
             'view/subject_info_views.xml',
             'view/coaching_menus.xml',],
    'author': "Meet",
    'application':True,
    'installable':True,
    # data files always loaded at installation
    # data files containing optionally loaded demonstration data
}
