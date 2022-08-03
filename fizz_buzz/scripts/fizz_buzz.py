#!/usr/bin/env python3

import argparse
import prompt
import sys
from fizz_buzz.fizz_buzz import fizz_buzz


DESCRIPTION = 'FizzBuzz task resolution CLI-utility'
GREETING = 'Welcome to Fizz Buzz!'
NUMBER_REQUEST = 'Number: '
PROG = 'fizz-buzz'
RULES = 'Submit a number and get an answer!'
USAGE = '%(prog)s [options]'


def main():
    fizz_buzz_args_parser = argparse.ArgumentParser(
        description=DESCRIPTION,
        prog=PROG,
        usage=USAGE
    )
    fizz_buzz_args_parser.parse_args()

    print(GREETING)
    print(RULES)

    try:
        while True:
            number = prompt.integer(NUMBER_REQUEST)
            print(fizz_buzz(number))
    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == '__main__':
    main()
