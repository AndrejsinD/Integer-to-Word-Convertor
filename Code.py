# The following code converts integer numbers to its English equivalent
# Author: David Andrejsin

from time import *

units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten","eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen","eighteen", "nineteen"]
tenfolds = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
HUNDRED = "hundred"
THOUSAND = "thousand"
NEGATIVE = "negative"

def one_digit_to_word(number):
    """Converts one digit to a word"""
    if int(number[-1]) == 0:
        return ""
    return units[int(number[-1])]

def two_digits_to_word(number):
    """Converts two digits to a word"""
    if int(number[-2]) == 0:
        return one_digit_to_word(number)
    if int(number[-2]) == 1:
        return teens[int(number[-1])]
    elif int(number[-1]) == 0:
        return tenfolds[int(number[-2])]
    else:
        return tenfolds[int(number[-2])] + "-" + one_digit_to_word(number)

def three_digits_to_word(number):
    """Converts three digits to a word"""
    if int(number[-3]) == 0:
        return two_digits_to_word(number)
    return units[int(number[-3])] + " " + HUNDRED + " " + two_digits_to_word(number)

def four_digits_to_word(number):
    """Converts four digits to a word"""
    if int(number[-4]) == 0:
        return three_digits_to_word(number)
    return units[int(number[-4])] + " " + THOUSAND + " " + three_digits_to_word(number)

def five_digits_to_word(number):
    """Converts fix digits to word"""
    if int(number[-5]) == 0:
        return four_digits_to_word(number)
    if int(number[-5]) == 1:
        return teens[int(number[-4])] + " " + THOUSAND + " " + three_digits_to_word(number)
    elif int(number[-4]) == 0:
        return tenfolds[int(number[-5])] + " " + THOUSAND + " " + three_digits_to_word(number)
    else:
        return tenfolds[int(number[-5])] + "-" + four_digits_to_word(number)

def six_digits_to_word(number):
    """Converts six digits to a word"""
    if int(number[-5]) == 0 and int(number[-4]) == 0:
        return units[int(number[-6])] + " " + HUNDRED + " " + THOUSAND + " " + three_digits_to_word(number)
    else:
        return units[int(number[-6])] + " " + HUNDRED + " " + five_digits_to_word(number)

def int_to_word(number):
    """Converts number input to a word"""
    if len(number) == 1:
        return one_digit_to_word(number)

    elif len(number) == 2:
        return two_digits_to_word(number)

    elif len(number) == 3:
        return three_digits_to_word(number)

    elif len(number) == 4:
        return four_digits_to_word(number)

    elif len(number) == 5:
        return five_digits_to_word(number)

    elif len(number) == 6:
        return six_digits_to_word(number)

def user_input():
    """
    - Asks for user input
    - Checks for a negative number
    - Handles zeros in front of the inputted number
    - Checks for a 'zero' result
    - Checks for an incorrect input
    - Returns final version of the word output
    """
    number = input("Enter number between -999999 and 999999: ")
    minus = False
    if number.startswith("-"):
        minus = True
        number = number[1:]

    while number.startswith("0"):
        number = number[1:] #removes all zeros from the beginning of the number

    if len(number) == 0:
        return(units[0])

    elif len(number) > 6:
        print("Incorrect input!")
        return user_input()

    else:
        try:
            number = int(number)
            number = str(number)
            if minus == False:
                return(int_to_word(number))
            else: return(NEGATIVE + " " + int_to_word(number))

        except:
            print("Incorrect input!")
            return user_input()

def all_numbers():
    """Prints all numbers in a range"""
    #bottom = int(input("What is the lowest number you want to print?"))
    #top = int(input("What is the highest number you want to print? "))
    for i in range(1000000):
        print(int_to_word(str(i)))
        #sleep(1/10)

def main():
    print(user_input())
    #all_numbers()

main()
