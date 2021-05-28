def is_leap_year(year):

    # Check if divisible by 4
    if year % 4 == 0:

        # Check if divisible by 100
        if year % 100 == 0:

            # Check if divisible by 400
            if year % 400 == 0:
                # It is a leap year
                return True

            else:
                return False

        else:
            return True
