def is_leap_year(year):

    # Check if divisible by 4
    if year % 4 == 0:

        # Check if divisible by 100
        if year % 100 == 0:

            # Check if divisible by 400
            if year % 400 == 0:
                # It is a leap year
                return True

            # Divisible by 4 and 100 but not 400 is non leap year
            else:
                return False

        # If divisible by 4 but not 100 then leap year
        else:
            return True

    # Non divisible by 4 so not leap year
    else:
        return False


def main():
    # Get user input for the year
    year_input = input("Enter a year: ")
    year = int(year_input)

    # Call leap year checker function
    is_leap_year(year)


if __name__ == "__main__":
    main()
