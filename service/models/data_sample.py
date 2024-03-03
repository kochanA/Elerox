from odoo import models, fields, api

class DataSample(models.Model):
    _name = "service.data.sample"
    _description = "Test Data Sample"

    name = fields.Char(string="Sample Name")
    price = fields.Float(string="Price")
    xyv = fields.Char(string="XYV")
    kkkk = fields.Float(string="kkk price")
    # testttt = fields.Char(string="Testtttt")




#service.acces_project_test,acces_project_test,service.model_project_test,base.group_user,1,1,1,1
