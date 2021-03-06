# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 INECO Part., Ltd. (<http://www.ineco.co.th>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name' : 'Ineco Point Of Sale',
    'version' : '0.1',
    'author' : 'INECO PART., LTD.',
    'category': 'INECO',
    'website' : 'http://www.ineco.co.th',
    'summary' : '',
    'description' : """
""",
    'depends' : ['point_of_sale','purchase','stock'
    ],
    'data' : [
        'point_of_sale_view.xml',
        'stock_view.xml',
        'security.xml',
    ],
    'update_xml' : [
    ],
    'installable' : True,
    'application' : False,
}
