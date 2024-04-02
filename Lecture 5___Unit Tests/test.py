# pip install pytest

from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(0) == 0
    assert square(-2) == 4
    assert square(-3) == 9
    assert square("cat") == 0
    
# when pytest find the first bug it stop there and don't go for every case
    

""""
-----> do not have to import pytest, rather execute via pytest keyword instead of python
-----> pytest do all of these thing automatically
-----> no need main function and function call
-----> just use assert keyword to check the case

-----> pytest test.py
-----> pytest file.py
"""