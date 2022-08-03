from fizz_buzz.fizz_buzz import (
    BUZZ, BUZZ_NUMBER, FIZZ, FIZZ_BUZZ, FIZZ_NUMBER, fizz_buzz
)

FIZZ_BUZZ_NUMBER = 15
JUST_NUMBER = 1
NOT_A_NUMBER = 'Not a number'


def test_fizz_buzz():
    assert fizz_buzz(JUST_NUMBER) == JUST_NUMBER
    assert fizz_buzz(FIZZ_NUMBER) == FIZZ
    assert fizz_buzz(BUZZ_NUMBER) == BUZZ
    assert fizz_buzz(FIZZ_BUZZ_NUMBER) == FIZZ_BUZZ
    assert fizz_buzz(NOT_A_NUMBER) is None
