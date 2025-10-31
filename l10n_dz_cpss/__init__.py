from . import models

def _preserve_tag_on_taxes(cr, registry):
    """
    Hook pour préserver les tags existants sur les taxes lors des mises à jour
    Utilise la fonction standard d'Odoo pour éviter la perte de configuration
    """
    from odoo.addons.account.models.chart_template import preserve_existing_tags_on_taxes
    preserve_existing_tags_on_taxes(cr, registry, 'l10n_dz_cpss')