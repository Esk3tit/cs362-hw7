def fizzbuzz(num):

    # FizzBuzz print (if multiple of 3 and 5)
    # Check this first because we if do the others first then we would already
    # print Fizz because the number is a multiple of 3 but we check it before
    # also checking if it is a multiple of 5 for FizzBuzz
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")

    # Fizz print (if multiple of 3)
    elif num % 3 == 0:
        print("Fizz")

    # Buzz print (if multiple of 5)
    elif num % 5 == 0:
        print("Buzz")

    # Else just print the number
    else:
        print(num)


def print_range():
    # Print from 1 to 100 (ending range value is EXCLUSIVE)
    for i in range(1, 101):
        fizzbuzz(i)


# Run print_range automatically if we execute this python file directly
if __name__ == "__main__":
    print_range()
