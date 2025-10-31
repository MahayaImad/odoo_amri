# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

{
    'name': "Comptabilité - Algérie CPSS",
    'summary': """ Plan comptable aux normes algériennes - Version CPSS. """,
    'description': """
Plan comptable algérien CPSS
============================

Ce module fournit :
* Plan comptable conforme aux normes algériennes
* Taxes algériennes (TVA, etc.)
* Positions fiscales
* Codes d'activité
* Formes juridiques
* Champs spécifiques aux entreprises algériennes (NIS, NIF, RC, AI)
* Configuration des rapports avec secteur d'activité

Adapté pour Odoo 18.0
""",

    'category': 'Accounting/Localizations/Account Charts',
    'version': '18.0.1.0',

    "contributors": [
        "Migration Odoo 18 - CPSS Version",
    ],
    'sequence': 1,

    'author': 'CPSS Solutions',
    'website': 'https://www.cpss.com',

    "license": "LGPL-3",
    "price": 0.0,
    "currency": 'EUR',

    'depends': [
        'base',
        'account',
        'sale',
        'sale_management',
    ],

    'assets': {
        'web.assets_backend': [
            "l10n_dz_cpss/static/src/js/many_tags_link.js",
        ],
    },

    'data': [
        # Sécurité d'abord
        'security/ir.model.access.csv',
        'security/rules.xml',

        # Données de base
        'data/default_data.xml',
        'data/l10n_dz_base_chart_data.xml',
        'data/account_group.xml',
        'data/account_account_template_data.xml',
        'data/account_chart_template_data.xml',
        'data/account_tax_data.xml',
        'data/account_fiscal_position_template_data.xml',
        'data/account_chart_template_configure_data.xml',
        'data/company_function.xml',

        # Vues
        "views/forme_juridique.xml",
        "views/activity_code.xml",
        "views/res_company.xml",
        "views/res_partner.xml",
        "views/configuration_settings.xml",
    ],

    'images': ['images/banner.gif'],

    'post_init_hook': '_preserve_tag_on_taxes',

    'installable': True,
    'auto_install': False,
    'application': False,
}