from mydb import MyDB

import pytest

@pytest.fixture(scope="module") # this way we will set up the cursor only once.
def cursorFixture():
    print("setting up")
    db = MyDB()
    conn = db.connect('server')
    cursor = conn.cursor()
    yield cursor #we will get to this point only after all references of cursor are passed to the relavant tests.
    conn.close()
    cursor.close()
    print(" teardown complete")


def test_johns_id(cursorFixture):
    id = cursorFixture.execute("select id from employee_db where name=John")
    assert id == 123

def test_toms_id(cursorFixture):
    id = cursorFixture.execute("select id from employee_db where name=Tom")
    assert id == 739
