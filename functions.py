"""def hello_fun():
    print("Hi Functions")

hello_fun()"""


"""def hello_function():
    return "Hi Saurabh"

print(hello_function())
#uppercase
print(hello_function().upper())"""

"""def hello_function(greeting, name):
    return '{}, {} Function.'.format(greeting, name)
print(hello_function("Hi", 'Saurabh'))"""

"""def sturent_info(*args, **kwargs):
    print(args)
    print(kwargs)

course = ['math', 'science']
info = {'name' : 'Ravi', 'age' : 22}

sturent_info(*course, **info )"""


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2017, 2))
