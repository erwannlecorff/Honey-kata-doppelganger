from calculator import Calculator
from tests.authorizer import Authorizer
import pytest


def test_divide_should_raise_error_when_not_authorized():
    # TODO: write a test that fails due to the bug in
    authorizer = Authorizer(False)
    calc = Calculator(authorizer)
    try:
        calc.divide(1, 2)
    except Exception as e:
        pass
    else:
        pytest.fail("Test failed")
