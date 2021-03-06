from anbardari.database_communication import create_table

import json
from anbardari.database_communication import c

entities = {
    'goods': {
        'attrs_list': [
            ('barcode', 'integer'),
            ('code', 'integer'),
            ('name', 'text'),
            ('group_title', 'text'),
            ('base_price', 'real'),
            ('price', 'real'),
            ('maintenance', 'text'),
            ('production_date', 'numeric'),
            ('entry_date', 'numeric'),
            ('exit_date', 'numeric'),
            ('producer', 'text'),
        ]
    },
    'team': {
        'attrs_list': [
            ('title', 'text'),
            ('maintenance', 'text'),
            ('base_price', 'real'),
        ]
    },
    'person': {
        'attrs_list': [
            ('name', 'text'),
            ('national_code', 'integer'),
            ('membership_code', 'integer'),
            ('birth_date', 'numeric'),
        ]
    },
    'member': {
        'attrs_list': [
            ('name', 'text'),
            ('code', 'integer'),
            ('password', 'text'),
        ]
    },
    'company': {
        'attrs_list': [
            ('name', 'text'),
            ('membership_code', 'integer'),
            ('registration_code', 'integer'),
        ]
    },
    'staff': {
        'attrs_list': [
            ('national_code', 'integer'),
            ('name', 'text'),
            ('personnel_code', 'text'),
            ('phone_number', 'integer'),
        ]
    },
    'transferee': {
        'attrs_list': [
            ('national_code', 'integer'),
            ('name', 'text'),
            ('personnel_code', 'text'),
            ('phone_number', 'integer'),
            ('work_hours', 'real'),
        ]
    },
    'dischargerer': {
        'attrs_list': [
                ('national_code', 'integer'),
                ('name', 'text'),
                ('personnel_code', 'text'),
                ('phone_number', 'integer'),
                ('work_hours', 'real'),
            ]
    },
    'transferer': {
        'attrs_list': [
            ('national_code', 'integer'),
            ('name', 'text'),
            ('personnel_code', 'text'),
            ('phone_number', 'integer'),
            ('work_hours', 'real'),
        ]
    },
    'keeper': {
        'attrs_list': [
            ('national_code', 'integer'),
            ('name', 'text'),
            ('personnel_code', 'text'),
            ('phone_number', 'integer'),
            ('work_hours', 'real'),
        ]
    },
    'not_being_adjacent': {
        'attrs_list': [
            ('title1', 'text'),
            ('title2', 'text'),
        ]
    },
    'instruction': {
        'attrs_list': [
            ('code', 'integer'),
            ('good_code', 'integer'),
            ('member_code', 'integer'),
            ('dischargerer_personal_code', 'integer'),
            ('date', 'numeric'),
        ]
    },
    'transfer': {
        'attrs_list': [
            ('code', 'integer'),
            ('good_code', 'integer'),
            ('member_code', 'integer'),
            ('transferee_personal_code', 'integer'),
            ('date', 'numeric'),
        ]
    },
    'recieve': {
        'attrs_list': [
            ('code', 'integer'),
            ('good_code', 'integer'),
            ('member_code', 'integer'),
            ('transferer_personal_code', 'integer'),
            ('date', 'numeric'),
            ('cost', 'real'),
        ]
    },
    'caring': {
        'attrs_list': [
            ('good_code', 'integer'),
            ('keeper_personal_code', 'integer'),
        ]
    },
    'member_basket': {
        'attrs_list': [
            ('member_code', 'integer'),
            ('member_goods_code', 'integer')
        ],
        'foreign_keys': [
            ('member_goods_code', 'goods(code)')
        ],
    },
}


for entity_name, entity_info in entities.iteritems():
    # c.execute('DROP TABLE if exists %s' % entity_name)
    create_table(entity_name, entity_info)