from calculator import square
import pytest

# each function is a individual test 

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0
    
def test_str():
    # when we expect an error
    with pytest.raises(TypeError):
        square("cat")

# if we assume that there can be raise any type of error
# if there is no error then our assumption is wrong so test failed
# if there is error which we assum then that test passed