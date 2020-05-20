"""
CTEC 121
<Grant Parkinson>
<assignment/lab name>
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

'''
def song(name):
    print(name, "finger,", name, "finger, where are you?")
    print("Here I am, here I am. How do you do?\n")


def sing():
    song("Daddy")
    song("Mommy")
    song("Brother")
    song("Sister")
    song("Baby")


def main():
    sing()

'''


def age_input(age):

    if 0 <= age <= 1:
        return 'I'
    elif 1 <= age < 13:
        return 'C'
    elif 13 <= age < 18:
        return 'T'
    elif 18 <= age < 123:
        return 'A'
    else:
        return 'Input a valid age range'


def unit_test():
    print(age_input(1))
    print(age_input(6))
    print(age_input(15))
    print(age_input(50))
    print(age_input(-12))
    print(age_input(200))
    print()


unit_test()


def main():
    print(age_input(1))


main()
