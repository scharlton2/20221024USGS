import pytest
from unittest.mock import Mock

HAM_VALUE = 42
ham = Mock()  # Create mock version of ham() function
ham.return_value = HAM_VALUE


# system under test
class Spam():  # System (class) under test
    def __init__(self, param):
        self._value = ham(param)  # Calls ham() (doesn't know if it's fake)

    @property
    def value(self):  # Property to return result of ham()
        return self._value

# dependency to be mocked -- not used in test
# def ham(n):
#     pass

def test_spam_calls_ham():   # Actual unit test
    s = Spam(HAM_VALUE)  # Create instance of Spam, which calls ham()
    ham.assert_called_once_with(HAM_VALUE)  # Check that spam.value correctly returns return value of ham()
    assert s.value == HAM_VALUE

if __name__ == '__main__':
    pytest.main([__file__])
