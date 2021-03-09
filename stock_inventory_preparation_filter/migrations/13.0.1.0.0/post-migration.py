# Copyright 2020 Tecnativa - Sergio Teruel
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from openupgradelib import openupgrade


def convert_m2o_to_x2m_fields(env):
    categ_column = openupgrade.get_legacy_name("category_id")
    if openupgrade.column_exists(env.cr, categ_column):
        openupgrade.m2o_to_x2m(
            env.cr,
            env["stock.inventory"],
            "stock_inventory",
            "categ_ids",
            categ_column,
        )
    lot_column = openupgrade.get_legacy_name("lot_column")
    if openupgrade.column_exists(env.cr, lot_column):
        openupgrade.m2o_to_x2m(
            env.cr,
            env["stock.inventory"],
            "stock_inventory",
            "lot_ids",
            openupgrade.get_legacy_name("lot_id"),
        )


@openupgrade.migrate()
def migrate(env, version):
    convert_m2o_to_x2m_fields(env)