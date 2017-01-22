from gluon.tools import Mail
import imaplib
import email
from email.header import decode_header

import random
import string
def index():
    groups = db(db.groups).select(db.groups.ALL)
    return locals()

# @auth.requires_login()
def create():
    form = SQLFORM(db.groups, deletable=True).process()
    if form.accepted:
        
        redirect(URL('index'))
    return locals()

def join():
    groups = db(db.groups).select(db.groups.group_code)
    form = SQLFORM(db.join_group, deletable=True).process()
    if form.accepted:
        for groups in groups:
            # response.flash = groups.group_code
            if request.vars.join_code in groups.group_code:
                response.flash = 'Welcome to the group!'
                redirect(URL('index'))
    return locals()

# @auth.requires_login()
def ecreate():
    form = SQLFORM(db.event, deletable=True).process()
    if form.accepted:
        redirect(URL('index'))
    return locals()

import json
from datetime import datetime
from json import dumps
# @auth.requires_login()
def event_page():
    #currently faulty, returns all events
    g = db.groups(request.args(0,cast=int)) or redirect(URL('index'))
    db.event.event_id.default = g.id
    db.event.event_code.default = g.group_code
    # event = db(db.event.event_id == g.id).select()
    event = db(db.event).select(db.event.ALL)
    json_data = json.dumps([[e.event_allDay, e.event_name, e.event_id, e.start.strftime("%B %d, %Y"), e.end.strftime("%B %d, %Y"), e.event_description] for e in event])
    response.flash = json_data

    return locals()

def user():
    return dict(form=auth())

def download():
    return response.download(request, db)

def picture():
    return response.view(request, db)

def getdata():
    rows = db().select(db.realtimedata.id, db.realtimedata.FlowRate,
                       limitby=(0, 3), orderby=~db.realtimedata.id)
    return json.dumps([[r.id, r.FlowRate] for r in rows])