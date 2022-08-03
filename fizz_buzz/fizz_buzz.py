BUZZ = 'Buzz!'
BUZZ_NUMBER = 5
FIZZ = 'Fizz!'
FIZZ_BUZZ = 'FizzBuzz!'
FIZZ_NUMBER = 3


def fizz_buzz(number):
    if not isinstance(number, int):
        return

    divisible_by_3 = not number % FIZZ_NUMBER
    divisible_by_5 = not number % BUZZ_NUMBER

    result = number

    if divisible_by_3 and divisible_by_5:
        result = FIZZ_BUZZ
    elif divisible_by_5:
        result = BUZZ
    elif divisible_by_3:
        result = FIZZ

    return result
