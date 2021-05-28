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
