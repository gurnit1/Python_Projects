# Subreddit Programming Prompts:
# https://www.reddit.com/r/ProgrammingPrompts/comments/457nkn/easy_make_an_ascii_summation_calculator/


def get_day_of_week(date):
    month = int(date[0:2])
    day = int(date[3:5])
    year = int(date[6:10])

    DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    DAY_OF_WEEK = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    result = ((year - 1900) * 365) + ((year - 1900) / 4)

    if (year - 1900) % 4 == 0 and month < 3:
        result -= 1

    for i in range(0, month - 1):
        result += DAYS_PER_MONTH[i]

    result += day

    print date + " falls on a " + DAY_OF_WEEK[result % 7]


print "Enter date in format MM-DD-YYYY: "
get_day_of_week(raw_input())
