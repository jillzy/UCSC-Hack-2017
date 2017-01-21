db = DAL("sqlite://storage.sqlite")

from gluon.tools import Auth
auth = Auth(db)
auth.define_tables(username=True)


db.define_table('groups',
                Field('group_name', 'string'),
                Field('group_code', 'integer'))

db.define_table('event',
                Field('event_name', 'string'),
                Field('event_description', 'text'),
                Field('event_code', 'integer'),
                Field('event_sdate', 'datetime'),
                Field('event_edate', 'datetime'),
                Field('event_stime', 'time'),
                Field('event_etime', 'time'))

# import gluon.template

# markmin_dict = dict(
#     code_python=lambda code: str(CODE(code)),
#     template=lambda
#     code: gluon.template.render(code, context=globals()),
#     sup=lambda
#     code: '<sup style="font-size:0.5em;">%s</sup>' % code,
#     br=lambda n: '<br>' * int(n),
#     groupdates=lambda group: group_feed_reader(group),
# )


# def get_content(b=None,
#                 c=request.controller,
#                 f=request.function,
#                 l='en',
#                 format='markmin'):
#     """Gets and renders the file in
#     <app>/private/content/<lang>/<controller>/<function>/<block>.<format>
#     """

#     def openfile():
#         import os
#         path = os.path.join(
#             request.folder, 'private', 'content', l, c, f, b + '.' + format)
#         return open(path)

#     try:
#         openedfile = openfile()
#     except Exception, IOError:
#         l = 'en'
#         openedfile = openfile()

#     if format == 'markmin':
#         html = MARKMIN(str(T(openedfile.read())), markmin_dict)
#     else:
#         html = str(T(openedfile.read()))
#     openedfile.close()

#     return html
