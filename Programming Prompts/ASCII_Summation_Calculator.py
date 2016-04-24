# Subreddit Programming Prompts:
# https://www.reddit.com/r/ProgrammingPrompts/comments/457nkn/easy_make_an_ascii_summation_calculator/


def ascii_sum(str):
    total = 0
    for letter in str:
        total += ord(letter)
    print total

print "Enter string that you wish to get total of: "
ascii_sum(raw_input())
