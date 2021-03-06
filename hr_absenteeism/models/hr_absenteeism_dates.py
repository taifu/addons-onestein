# Copyright 2016-2018 Onestein (<http://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class HrAbsenteeismDates(models.Model):
    _name = "hr.absenteeism.dates"
    _description = "Absenteeism Notification Dates"

    name = fields.Char("Notification Name")
    absent_notify_date = fields.Datetime("Absent Notification Date")
    holiday_id = fields.Many2one(
        "hr.holidays",
        string="Related Holiday",
        ondelete="cascade"
    )
    notification_id = fields.Many2one(
        "hr.absenteeism.notifications",
        string="Related notification"
    )
