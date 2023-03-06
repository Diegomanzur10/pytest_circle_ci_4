from code.main import suma, resta, multiplication, division
import pytest


@pytest.mark.parametrize(
        (
            "a",
            "b",
            "c"
        ),
        [
            (
                1,
                2,
                3,
            ),
            (
                -1,
                -2,
                -3
            )
        ],
        ids = [
            "Test1",
            "Test2"
        ]
)
def test_suma(a, b, c):
    assert suma(a, b) == c

@pytest.mark.skip(reason = "Funcion a depricar")
def test_division():
    assert division(3, 0) == 1

