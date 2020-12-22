"""
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
Your task is simple - convert the input date and time from computer format into a "human" format.

Input: Date and time as a string

Output: The same date and time, but in a more readable format
"""


def date_time(time: str) -> str:
    day = int(time[:2])
    month = int(time[3:5])
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
    year = int(time[6:10])
    num_h = int(time[11:13])
    hours = str(num_h) + ' hour' if num_h == 1 else str(num_h) + ' hours'
    num_m = int(time[14:])
    mnts = str(num_m) + ' minute' if num_m == 1 else str(num_m) + ' minutes'
    return f'{day} {month_list[month - 1]} {year} year {hours} {mnts}'


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
