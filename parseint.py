# How would you change a string of numbers into an integer?
#
#

# parseInt basically

# "" => 0
# "-" => negative
# don't worry about decimal point rn

nums = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}

def parse(string):

    negative = False

    if string == "":
        return 0
    elif string[0] == "-":
        # negative
        negative = True
        string = string[1:]

    # go through the number, chopping off the front number each time
    n = 0

    while string != "":
        # chop off front number
        first_char = string[0]
        string = string[1:]

        # multiply last digit
        n *= 10

        # tack on the last char
        n += nums[first_char]


    if negative:
        n *= -1

    return n



print parse("-1234") + 5
print parse("0") + 5
print parse("5") + 5
print parse("17") + 5
