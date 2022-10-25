import sqlite3
from collections import namedtuple
import pytest

# conn = sqlite3.connect('DATA/presidents.db')
# cursor = conn.cursor()

Person = namedtuple('Person', 'first_name last_name')  # create object to test

FIRST_NAME = "Guido"
LAST_NAME = "Von Rossum"

# @pytest.fixture()
# def presidents():
#     cursor.execute("select last_name from presidents")
#     return cursor.fetchall()

@pytest.fixture  # mark person as a fixture
def person():
    """
    Return a 'Person' named tuple with fields 'first_name' and 'last_name'
    """
    return Person(FIRST_NAME, LAST_NAME)  # return value of fixture

@pytest.fixture
def notes():
    return 'do', 're', 'mi'

def test_first_name(person):  # pass fixture as test parameter
    assert person.first_name == FIRST_NAME

def test_last_name(person):  # pass fixture as test parameter
    assert person.last_name == LAST_NAME

def test_do_in_notes(notes):
    assert 'do' in notes

