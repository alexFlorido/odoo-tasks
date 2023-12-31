from xmlrpc import client
url='http://localhost:8069'
db='test1'
username='alexflorido0897@gmail.com'
password='admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models =  client.ServerProxy("{}/xmlrpc/2/object".format(url))
model_access = models.execute_kw(db, uid, password,
                                 'academy.course', 'check_access_rights',
                                 ['write'], {'raise_exception': False})
print(model_access)

courses = models.execute_kw(db, uid, password,'academy.course', 'search_read',[[['level','in',['intermediate','beginner']]]])
print(courses)

course = models.execute_kw(db, uid, password, 'academy.course', 'search', [[['name','=','Accounting 200']]])
print(course)

session_field = models.execute_kw(db, uid, password,'academy.session', 'fields_get', [], {'attributes': ['string', 'type', 'required']})
print(session_field)

new_session = models.execute(db, uid, password,
                             'academy.session', 'create',
                             [
                                 {
                                     'course_id': course[0],
                                     'duration': 5,
                                 }
                             ])
print(new_session)