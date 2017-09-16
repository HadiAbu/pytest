from mydb import MyDB

conn = None
cur = None

def setup_module(module):
    global conn
    global cur
    db = MyDB()
    conn = db.connect('server')
    cur = conn.cursor()

def test_johns_id():
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_toms_id():
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 739


def teardown_module(module):
    conn.close()
    cur.close()
