# Copyright 2015-${DATE} Alia Technologies, S.L. - http://www.alialabs.com
# @author: Alia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
   'name': 'HelpDesk Curso ',
   'summary': 'AEDOO Curso 2020',
   'version': '13.0.1.0.0',
   'author': 'Sidro',
   'website': '',
   'category': 'AEDOO',
   'license': 'AGPL-3',
   'contributors': [
       'Sidro Vázquez <sidro.vazquez@alialabs.com>',
   ],
   'maintainers': [
       'Sidro Vázquez <sidro.vazquez@alialabs.com>',
   ],
   'description': '''
       AEDOO Curso 2020.
   ''',
   'depends': [
       # Project Dependencies
       # Base Dependencies
   ],
   'demo': [],
   'data': [
       # Security
       'security/helpdesk_security.xml',
       'security/ir.model.access.csv',
       # Data
       # Views
       'views/helpdesk_ticket_views.xml',
   ],
   'qweb': [],
   'demo': [],
   'test': [],
   'installable': True,
   'auto_install': False,
   'application': False,
   'sequence': 10,
}
