from src.main import add_int


def test_add_int() -> None:
    assert add_int(1, 2) == 3
    assert add_int(1, 2) == 6
