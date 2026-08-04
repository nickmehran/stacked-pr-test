from greeting import farewell, greet


def test_greet():
    assert greet("World") == "Hello, World!"


def test_farewell():
    assert farewell("World") == "Goodbye, World!"
