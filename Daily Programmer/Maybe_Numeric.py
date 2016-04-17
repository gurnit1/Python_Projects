# Subreddit Daily Programmer Challenge 262:
# https://www.reddit.com/r/dailyprogrammer/comments/4eaeff/20160411_challenge_262_easy_maybenumeric/

def numeric_or_string(val):
    try:
        num = float(val)
        numeric = isinstance(num, float)
        if numeric:
            print "number"
    except Exception:
        print "string"

print "Enter value: "
numeric_or_string(raw_input())