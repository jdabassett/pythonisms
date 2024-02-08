import pytest

from module.decorator import timer

assert (pytest and timer), "one or more modules not successfully imported: test_decorator.py file"


# @pytest.mark.skip()
def test_timer_exists():
    assert timer


# @pytest.mark.skip()
def test_timer_list(return_list_function):
    value = return_list_function()
    assert value == [1,2,3]


@pytest.fixture
def return_list_function():
    @timer
    def return_list():
        return [1,2,3]
    return return_list
