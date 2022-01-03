import calendar
import datetime as dt

cal = calendar.TextCalendar()

holidays = [(dt.date(2022, 4, 11), dt.date(2022, 5, 9)),
            (dt.date(2022, 6, 6), dt.date(2022, 7, 7)),
            (dt.date(2022, 9, 9), dt.date(2022, 10, 20))]


# def days_on_holiday(holiday_endpoints):
#     """Returns every day between an arbitrary amount of endpoints."""
#     days = []
#     for start, end in holiday_endpoints:
#         days.extend(days_between(start, end))
#     return days


def print_holidays(holiday_endpoints):
    for start, end in holiday_endpoints:
        print(f"From {start} to {end}")


def total_days(dates):
    """Counts the number of days between a list of date endpoints"""
    return sum((end - start).days + 1 for start, end in dates)


def days_forward(date):
    """Returns the final day in an 180 rolling day window"""
    return date + dt.timedelta(days=179)


def days_between(day1, day2):
    """Returns all the days between two dates (inclusive)."""
    diff = day2 - day1
    for i in range(diff.days + 1):
        yield day1 + dt.timedelta(days=i)


def date_is_holiday(date, holiday_endpoints):
    """Returns if a date lies within the span of any given holiday."""
    return any(start <= date <= end for start, end in holiday_endpoints)


def validate_holiday(start, end, holiday_endpoints):
    new_holiday_endpoints = holiday_endpoints + [(start, end)]
    days_used = days_in_schengen(new_holiday_endpoints)
    return days_used, days_used <= 90


def days_in_schengen(holiday_end_points):
    final_exit = sorted(holiday_end_points)[-1][1]  # Second element of final holiday
    ordinal_date = final_exit - dt.timedelta(days=179)

    days_used = sum(1 for day in days_between(ordinal_date, final_exit) if date_is_holiday(day, holiday_end_points))
    return days_used


# def validate_all_holidays(provisional_holiday_endpoints, curr_holiday_endpoints):
#     holidays_copy = curr_holiday_endpoints[:]
#     days_used = 0
#     for start, end in provisional_holiday_endpoints:
#         days_used, valid = validate_holiday(start, end, holidays_copy)
#         if valid:
#             holidays_copy.append((start, end))
#         else:
#             print(f"Invalid holiday span from {start} to {end} using {days_used} days")
#     return holidays_copy, days_used


def enter_date():
    FORMAT = "%Y-%m-%d"
    print("Please enter the start end end dates of your holiday separated by a comma")
    print("example 2022-5-5, 2022-6-6")

    answer = input()
    start, end = answer.replace(" ", "").split(",")
    start_date, end_date = dt.datetime.strptime(start, FORMAT).date(), dt.datetime.strptime(end, FORMAT).date()
    return start_date, end_date

# new_endpoints, days = validate_all_holidays([(dt.date(2022, 4, 11), dt.date(2022, 5, 9)),
#                                        (dt.date(2022, 6, 6), dt.date(2022, 7, 7)),
#                                        (dt.date(2022, 9, 9), dt.date(2022, 10, 20))], holidays)
#
# if days <= 90:
#     print(f"Valid dates: You have spent {days} in the Schengen area with {90 - days} remaining.")
# print_holidays(new_endpoints)
