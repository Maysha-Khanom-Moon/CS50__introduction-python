from hello import hello

# pytest test_hello.py
def test_default():
    assert hello() == "hello, world"
    
    
def test_hellO():
    assert hello("David") == "hello, David"
    
def test_agrument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"