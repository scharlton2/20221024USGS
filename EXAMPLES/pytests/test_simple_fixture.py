import sqlite3
from collections import namedtuple
import pytest

conn = sqlite3.connect('../../DATA/presidents.db')
cursor = conn.cursor()

Person = namedtuple('Person', 'first_name last_name')  # create object to test

FIRST_NAME = "Guido"
LAST_NAME = "Von Rossum"

def pi():
    return 22 / 7

def test_pi_greater_than_three():
    assert pi() > 3

@pytest.fixture()
def presidents():
    """
    Provide list of last names of presidents
    """
    cursor.execute("select lastname from presidents")
    return [p[0] for p in cursor.fetchall()]  # data is a list containing one tuple for each row

@pytest.fixture  # mark person as a fixture
def person():
    """
    Return a 'Person' named tuple with fields 'first_name' and 'last_name'
    """
    return Person(FIRST_NAME, LAST_NAME)  # return value of fixture

@pytest.fixture
def notes():
    return 'do', 're', 'mi'

class TestExtraStuff:
    def test_buchanan_in_president_names(self, presidents):
        assert "Buchanan" in presidents

    def test_do_in_notes(self, notes):
        assert 'do' in notes

def test_first_name(person):  # pass fixture as test parameter
    assert person.first_name == FIRST_NAME

def test_last_name(person):  # pass fixture as test parameter
    assert person.last_name == LAST_NAME


