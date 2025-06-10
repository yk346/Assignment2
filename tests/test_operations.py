from app.operations import addition

def test_addition():
    assert addition(1,1) == 2

def test_substraction():
    assert substraction(1,1) == 0

def test_multiplication():
    assert multiplication(1,1) == 1