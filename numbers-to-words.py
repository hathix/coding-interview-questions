# How would you change an integer into word form?
# e.g. 1234 = one thousand two hundred thirty-four

digits = ["zero","one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["zero","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def convert_two_digits(num):
    if num < 10:
        return digits[num]
    elif num < 20:
        return teens[num - 10]
    else:
        ones_place = num % 10
        tens_place = num / 10
        if ones_place > 0:
            return tens[tens_place] + "-" + digits[ones_place]
        else:
            return tens[tens_place]

def convert(num):
    if num < 100:
        return convert_two_digits(num)

    if num < 1000:
        hundreds_place = num / 100
        last_two = num % 100
        return digits[hundreds_place] + " hundred " + convert_two_digits(last_two)

    if num < 1000000:
        num_thousands = num / 1000
        thousands_string = convert(num_thousands)
        last_three = num % 1000
        last_three_string = convert(last_three)
        return thousands_string + " thousand " + last_three_string


print convert(67)
# bug: this prints "one hundred zero" :(
print convert(100)
print convert(150)
