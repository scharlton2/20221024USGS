import pytest  # <1>
import hamlib  # <2>

HAM_ARG = 8

class Barbecue():  # <3>

    def doit(self):  # <4>
        return hamlib.ham(HAM_ARG)

def test_barbecue_doit_calls_ham(mocker):   # <5>
    mocker.patch('hamlib.ham')  # <6>
    b = Barbecue()
    result = b.doit()
    hamlib.ham.assert_called_once_with(HAM_ARG)  # <9>

if __name__ == '__main__':
    pytest.main([__file__, '-s'])   # <10>
