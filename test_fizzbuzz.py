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
    for i in [5, 10, 25]:
        fizzbuzz.fizzbuzz(i)
        # capture printed output on stdout to test
        captured = capsys.readouterr()

        # Assert test on captured output
        # Note: print in python adds newline so check for it too
        assert captured.out == "Buzz\n"


def test_fizzbuzz(capsys):
    # Use for loop to test a few numbers that are multiples of 3 and 5
    for i in [15, 30, 45]:
        fizzbuzz.fizzbuzz(i)
        # capture printed output on stdout to test
        captured = capsys.readouterr()

        # Assert test on captured output
        # Note: print in python adds newline so check for it too
        assert captured.out == "FizzBuzz\n"


def test_other(capsys):
    # Use for loop to test a few numbers that are not multiples of 3 and 5
    for i in [1, 2, 4]:
        fizzbuzz.fizzbuzz(i)
        # capture printed output on stdout to test
        captured = capsys.readouterr()

        # Assert test on captured output
        # Note: print in python adds newline so check for it too
        assert captured.out == str(i) + "\n"
