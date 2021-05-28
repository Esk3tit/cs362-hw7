import leap_year


# Test leap years
def test_leap_years():
    assert leap_year.is_leap_year(2016)
    assert leap_year.is_leap_year(2000)


# Test non leap years
def test_non_leap_years():
    assert leap_year.is_leap_year(1999) is False
    assert leap_year.is_leap_year(2100) is False
