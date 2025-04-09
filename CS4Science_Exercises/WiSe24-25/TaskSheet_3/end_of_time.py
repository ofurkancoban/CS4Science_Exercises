# End of time - when?
# Coban, Omer Furkan
# WiSe 24/25
# CS4Science - Team B2

# constants
seconds_in_a_year = 365.24219052 * 24 * 60 * 60  # average seconds in a year
seconds_in_a_day = 24 * 60 * 60  # seconds in a day
max_signed_int_32 = 2**31 - 1  # maximum 32-bit signed integer
max_unsigned_int_32 = 2**32 - 1  # maximum 32-bit unsigned integer

# month lengths (not accounting for leap years here, will handle later)
month_length = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

# helper function to compute the last date
def compute_last_date(seconds):
    rest_seconds = seconds
    year = 1970

    # calculate the last year
    while rest_seconds >= seconds_in_a_year:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # leap year
            rest_seconds -= 366 * seconds_in_a_day
        else:
            rest_seconds -= 365 * seconds_in_a_day
        year += 1

    # check for leap year
    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    month_lengths = list(month_length)
    if is_leap_year:
        month_lengths[1] = 29  # adjust for leap year february

    # calculate the last month and day
    month = 0
    for m_days in month_lengths:
        seconds_in_month = m_days * seconds_in_a_day
        if rest_seconds < seconds_in_month:
            break
        rest_seconds -= seconds_in_month
        month += 1

    # remaining seconds determine the day
    day = rest_seconds // seconds_in_a_day + 1

    # return the result as a tuple (year, month, day)
    return year, month + 1, int(day)

# calculate results
last_date_signed = compute_last_date(max_signed_int_32)
last_date_unsigned = compute_last_date(max_unsigned_int_32)

# print results
print("last day of posix time with signed 32-bit integers: year {}, month {}, day {}".format(*last_date_signed))
print("last day of posix time with unsigned 32-bit integers: year {}, month {}, day {}".format(*last_date_unsigned))

# commentary
"""
2. last date with unsigned 32-bit integers: february 7, 2106
3. disadvantage of using unsigned integers:
   - using unsigned integers would prevent representation of negative time values, which are essential for representing dates and times before the posix epoch (january 1, 1970).
   - this loss of ability to work with historical dates could make the system less flexible for applications requiring backward time compatibility.
"""
