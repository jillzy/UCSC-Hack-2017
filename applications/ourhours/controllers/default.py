from gluon.tools import Mail
import imaplib
import email
from email.header import decode_header

mail = Mail()
mail.settings.server = 'smtp.gmail.com:587'
mail.settings.sender = 'ourhours1337@gmail.com'
mail.settings.login = 'ourhours1337@gmail.com:weslysmellsgood'

import random
import string


def index():
    groups = db(db.groups).select(db.groups.ALL)
    return locals()


def create():
    pw = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(5)])
    db.groups.group_code.default = pw
    form = SQLFORM(db.groups, deletable=True).process()
    if form.accepted:

        mail.send(to=[request.vars.email],
            subject="Password for " + request.vars.group_name,
            message= pw)
        redirect(URL('index'))
    return locals()

def join():
    groups = db(db.groups).select(db.groups.ALL)
    form = SQLFORM(db.join_group, deletable=True).process()
    if form.accepted:
        for groups in groups:
            if request.vars.join_code in groups.group_code:
                redirect(URL('event_page', args=groups.id))
            else:
                response.flash = "Incorrect join code"
    return locals()

def ecreate():
    form = SQLFORM(db.event, deletable=True).process()
    if form.accepted:
        redirect(URL('index'))
    return locals()

import json
from datetime import datetime
from json import dumps

def event_page():
    #currently faulty, returns all events
    g = db.groups(request.args(0,cast=int)) or redirect(URL('index'))
    db.event.event_id.default = g.id
    db.event.event_code.default = g.group_code
    event = db(db.event).select(db.event.ALL)
    json_data = json.dumps([[e.event_allDay, e.event_name, e.event_id, e.start.strftime("%B %d, %Y"), e.end.strftime("%B %d, %Y"), e.event_description] for e in event])
    return locals()

def user():
    return dict(form=auth())

def download():
    return response.download(request, db)

def picture():
    return response.view(request, db)