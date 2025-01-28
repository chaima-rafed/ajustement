{
    'name': 'Inventory Sessions',
    'version': '1.0.0',
    'category': 'Inventory',
    'summary': 'Compare stock counts between groups with discrepancies highlighted.',
    'description': """
        A module for managing inventory sessions where multiple groups count stock.
        - Automatically calculates differences (écart).
        - Highlights discrepancies in red and matches in green.
        - Allows manual entry of final quantities.
    """,
    'author': 'Titam_altex',
    'depends': ['stock','base','web'],
    'data': [
        'security/ir.model.access.csv',
        'views/inventory_session_views.xml',
        #'views/stock_quant_views.xml',
        'views/wizard.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
