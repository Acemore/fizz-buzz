import pytest
from fizz_buzz.fizz_buzz import fizz_buzz


@pytest.mark.parametrize(
    "input_data, output_answer",
    [
        (1, 1),
        (3, 'Fizz!'),
        (5, 'Buzz!'),
        (15, 'FizzBuzz!'),
        ('Not a number', None),
    ]
)
def test_fizz_buzz(input_data, output_answer):
    assert fizz_buzz(input_data) == output_answer
