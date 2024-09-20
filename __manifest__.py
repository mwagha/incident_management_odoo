# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "Team Incident Management",
  "summary"              :  """Team Incident Management""",
  "category"             :  "ODOO",
  "version"              :  "1.0.0",
  "sequence"             :  1,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://store.webkul.com/Odoo-Team-Incident-Management.html",
  "description"          :  """This module lets the employee to create incidents of different type such as communication, suggestion, testing etc.""",
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=incident_management",
  "depends"              :  ['project_advance_team'],
  "data"                 :  [
                             'security/incident_security.xml',
                             'security/ir.model.access.csv',
                             'wizard/reason_wizard_view.xml',
                             'views/team_incident_view.xml',
                            ],
  "demo"                 :  ['data/demo.xml'],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  50,
  "currency"             :  "USD",
  "pre_init_hook"        :  "pre_init_check",
}