from odoo import models, fields, api

class FormeJuridique(models.Model):
    _name = "forme.juridique"
    _description = "Forme juridique"
    _order = "name"

    name = fields.Char(string="Forme juridique", required=True, index=True, tracking=True)
    code = fields.Char(string="Code", index=True, tracking=True)
    company_id = fields.Many2one('res.company', string='Société', default=lambda self: self.env.company.id)

    def name_get(self):
        result = []
        for record in self:
            display_name = record.name
            if record.code:
                display_name = f"{record.code} - {record.name}"
            result.append((record.id, display_name))
        return result

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []
        if name:
            domain = ['|', ('name', operator, name), ('code', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)