# Subreddit Daily Programmer Ideas:
# https://www.reddit.com/r/dailyprogrammer_ideas/comments/3rjy1y/easy_ordinal_dates/

def get_ordinal_date(date):
    DAYS_PER_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if date.index('-') == 2:  # format mm-dd-yyyy
        month = int(date[0:2])
        day = int(date[3:5])
        year = int(date[6:10])
    else:  # format yyyy-mm-dd
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])

    days_total = 0

    for i in range(0, month - 1):
        days_total += DAYS_PER_MONTH[i]

    days_total += day

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) and (month > 2 or (month == 2 and month > 28)):
        # print "Leap year"
        days_total += 1
    print str(year) + "-" + str(days_total)

print "Enter date: "
get_ordinal_date(raw_input())
