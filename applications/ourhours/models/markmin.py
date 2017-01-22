db = DAL("sqlite://storage.sqlite")

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=True)

import random
import string

db.define_table('groups',
                Field('email', requires = IS_EMAIL(error_message='invalid email!')),
                Field('group_name', 'string'),
                Field('optional_group_photo', 'upload'),
                Field('group_code', 'string'),
                Field('group_description', 'text', requires=IS_LENGTH(maxsize=80), default='No Group Description.'))

db.define_table('event',
                Field('event_allDay', 'boolean'),
                Field('event_name', 'string'),
                Field('event_id', 'integer'),
                Field('event_description', 'text'),
                Field('event_code', 'string'),
                Field('start', 'datetime'),
                Field('end', 'datetime'))

db.define_table('join_group',
                Field('join_code', 'string'))


db.groups.group_code.writable = db.groups.group_code.readable = False
db.event.event_id.writable = db.event.event_id.readable = False
db.event.event_code.writable = db.event.event_code.readable = False