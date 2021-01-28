"""
As the input you’ll get the date of the first vacation day in the format 'YYYY-MM-DD' and the total number of vacation
days. Your task is to find out which day will be the first working day after the vacation. If it’ll be Saturday or
Sunday then it should be the next Monday.
In this mission you have to ignore national holidays and consider only Saturdays and Sundays.
Also don't forget about February 29th in the leap year and the situation when the vacation starts at the end of December
of the one year and ends at the beginning of the next year.

Input: The first day of the vacation and the number of days in it.

Output: The date of the first working day.
"""
from datetime import date, timedelta


def vacation(start_date, days):
    list_date = [int(i) for i in start_date.split('-')]
    work_day = date(list_date[0], list_date[1], list_date[2]) + timedelta(days=days)
    if work_day.weekday() == 5:
        return str(work_day + timedelta(days=2))
    elif work_day.weekday() == 6:
        return str(work_day + timedelta(days=1))
    else:
        return str(work_day)


if __name__ == '__main__':
    print("Example:")
    print(vacation('2018-07-01', 14))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert vacation('2018-07-01', 14) == '2018-07-16'
    assert vacation('2018-02-19', 10) == '2018-03-01'
    assert vacation('2000-02-28', 5) == '2000-03-06'
    assert vacation('1999-12-20', 14) == '2000-01-03'
    print("Coding complete? Click 'Check' to earn cool rewards!")
