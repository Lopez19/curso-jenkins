def suma(a: int, b: int) -> int:
    return a + b

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    assert suma(-5, -10) == -15
    assert suma(100, 200) == 300
    
def test_suma_failure():
    assert suma(2, 3) == 6  # This test will fail
    