# mkdir test
# code test/test_hello.py

from hello import hello


def test_default():
    assert hello() == "hello, world"
    

def test_argument():
    assert hello("David") == "hello, David"


"""
code test/__init__.py
----> An empty __init__.py file is still necessary to mark a directory as a package
----> so that folder works as a single file when we test it via pytest


----> pytest test: we can check all of the file of test folder at once
"""