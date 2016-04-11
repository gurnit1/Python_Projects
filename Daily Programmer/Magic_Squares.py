# Subreddit Daily Programmer Challenge 261:
# https://www.reddit.com/r/dailyprogrammer/comments/4dccix/20160404_challenge_261_easy_verifying_3x3_magic/


class MagicSquares:
    square = []

    def __init__(self):
        self.square = []

    def user_input(self, usr_input):
        usr_input = usr_input.replace(' ', '')
        self.square = usr_input.split(',')
        return self.square

    def validate_square(self):
        self.square = [int(s) for s in self.square if s.isdigit() and 0 < int(s) < 10]
        if len(self.square) != 9:
            return False
        return True

    def check_if_magic_square(self):
        if self.square[0] + self.square[1] + self.square[2] != 15:
            print 1
            return False
        if self.square[3] + self.square[4] + self.square[5] != 15:
            return False
        if self.square[6] + self.square[7] + self.square[8] != 15:
            return False
        if self.square[0] + self.square[4] + self.square[8] != 15:
            return False
        if self.square[2] + self.square[4] + self.square[6] != 15:
            return False
        return True

ms = MagicSquares()
print "Please input magic square list from left to right, top to bottom comma separated: "
usr_val = raw_input()
sqr = ms.user_input(usr_val)
if ms.validate_square():
    val = ms.check_if_magic_square()
    print val
else:
    print "Not a valid list of numbers"

