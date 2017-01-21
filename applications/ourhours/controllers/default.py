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
        response.flash = 'Successful'
    return locals()

# @auth.requires_login()
def ecreate():
    form = SQLFORM(db.event, deletable=True).process()
    if form.accepted:
        response.flash = 'Success'
        redirect(URL('index'))
    return locals()

# @auth.requires_login()
def event_page():
    #currently faulty, returns all events
    g = db.groups(request.args(0,cast=int)) or redirect(URL('index'))
    db.event.event_id.default = g.id
    db.event.event_code.default = g.group_code
    event = db(db.event.event_id == g.id).select()
    # event = db(db.event).select(db.event.ALL)
    return locals()

def user():
    return dict(form=auth())

def download():
    return response.download(request, db)

def picture():
    return response.view(request, db)