import fizzbuzz
import pytest


def test_fizz(capsys):
    # Use for loop to test a few numbers that are multiples of 3
    for i in [3, 6, 9]:
        fizzbuzz.fizzbuzz(i)
        # capture printed output on stdout to test
        captured = capsys.readouterr()

        # Assert test on captured output
        # Note: print in python adds newline so check for it too
        assert captured.out == "Fizz\n"

def test_buzz(capsys):
    # Use for loop to test a few numbers that are multiples of 5
    for i in [5, 10, 15]:
        fizzbuzz.fizzbuzz(i)
        # capture printed output on stdout to test
        captured = capsys.readouterr()

        # Assert test on captured output
        # Note: print in python adds newline so check for it too
        assert captured.out == "Buzz\n"