from re import match


def show_table(string_1, string_2):
    """Show two strings in formatted table"""
    print("/-"+"-"*len(string_1)+"---"+"-"*len(string_2)+"-\\")
    print("| {} | {} |".format(string_1, string_2))
    print("\\-"+"-"*len(string_1)+"---"+"-"*len(string_2)+"-/")

BINARY_SYSTEM = "2"
DECIMAL_SYSTEM = "10"

weight = 0
number_output = None

user_input = input()
user_input = user_input.split(" ")

if len(user_input) < 2:
    exit()

number = user_input[0]
number_lenght = len(number)
number_system = user_input[1]

if number_system == BINARY_SYSTEM:
    if match("[01]+$", number):
        number_output = 0
        while weight < number_lenght:
            number_output += int(number[-weight - 1]) * 2**weight
            weight += 1
        show_table(str(number_output), DECIMAL_SYSTEM)
    else:
        exit()

elif number_system == DECIMAL_SYSTEM:
    if number.isdecimal():
        number_output = ""
        number = int(number)
        if number == 0:
            number_output = "0"
        else:
            while number > 0:
                if number % 2:
                    number_output = "1" + number_output
                else:
                    number_output = "0" + number_output
                number //= 2
        show_table(number_output, BINARY_SYSTEM)
    else:
        exit()

else:
    exit()
