def multiplicacion(a: int, b: int) -> int:
    return a * b

def test_multiplicacion():
    assert multiplicacion(2, 3) == 6
    assert multiplicacion(-1, 1) == -1
    assert multiplicacion(0, 0) == 0
    assert multiplicacion(-5, -10) == 50
    assert multiplicacion(100, 200) == 20000
    