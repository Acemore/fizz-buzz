def fizz_buzz(number):
    if not isinstance(number, int):
        return

    divisible_by_3 = not number % 3
    divisible_by_5 = not number % 5

    result = number

    if divisible_by_3 and divisible_by_5:
        result = 'FizzBuzz!'
    elif divisible_by_5:
        result = 'Buzz!'
    elif divisible_by_3:
        result = 'Fizz!'

    return result
