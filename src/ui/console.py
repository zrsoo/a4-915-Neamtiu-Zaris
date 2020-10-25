"""
This is the user interface module. These functions call functions from the domain and functions module.
"""

# Imports

import domain.entity as entity
import tests.tests as tests
import functions.functions as functions
import copy

#

# Font customization


yellow = '\u001b[33m'  # Yellow text
endc = '\033[m'  # Reset to default text
blue = '\u001b[34m'  # Blue text
green = '\u001b[32m'  # Green text
red = '\u001b[31m'  # Red text
magenta = '\u001b[35m'  # Magenta text
cyan = '\u001b[36m'  # Cyan text
bblue = '\u001b[34;1m'  # Bright blue text
bold = '\u001b[1m'  # Bold text
underlined = '\u001b[4m'  # Underlined text


#


# UI section
# (all functions that have input or print statements, or that CALL functions with print / input are  here).
# Ideally, this section should not contain any calculations relevant to program functionalities

def do_remove(input_list, li_complex, nr_cmds):
    if nr_cmds == 2:  # if command is "remove x"

        index = functions.remove_single(input_list, li_complex)
        print("You have successfully removed the complex number at position " + str(index))

    elif nr_cmds == 4:  # if command is "remove x to y"

        eindex, sindex = functions.remove_multiple(input_list, li_complex)

        print("You have successfully removed the complex numbers from "
              "position " + str(sindex) + " to position " + str(eindex))


def do_list(input_list, li_complex, nr_cmds):
    if nr_cmds == 1:  # If the command is "list"
        print(yellow + "\nThe list of complex numbers is: " + endc)
        print_list(li_complex)

    elif nr_cmds == 5:  # If the command is "list real "x" to "y"
        list_real(input_list, li_complex)

    else:  # If the command is "list modulo '' x"
        list_modulus(input_list, li_complex)


def list_modulus(input_list, li_complex):
    comp = int(input_list[3])
    sgn = input_list[2]
    exists = False
    if sgn == "<":
        for nr in li_complex:
            if functions.complex_modulus(nr) < comp:
                print_complex(nr)
                exists = True
    elif sgn == "=":
        for nr in li_complex:
            if functions.complex_modulus(nr) == comp:
                print_complex(nr)
                exists = True
    elif sgn == ">":
        for nr in li_complex:
            if functions.complex_modulus(nr) > comp:
                print_complex(nr)
                exists = True
    if not exists:
        print("The list does not contain any number with the specified property.")


def list_real(input_list, li_complex):
    if input_list[1] != "real" or input_list[3] != "to":
        raise ValueError
    spos = int(input_list[2]) - 1
    epos = int(input_list[4]) - 1
    exists = False
    if spos < 0 or epos > len(li_complex):
        raise IndexError
    for index in range(spos, epos + 1):
        if entity.get_imaginaryp(li_complex[index]) == 0:
            print_complex(li_complex[index])
            exists = True
    if not exists:
        print("The list does not contain any real numbers in that interval.")


def print_menu():
    """Prints the user menu"""

    print(bold + underlined + "\nList of commands:", endc + "\n")
    print(green + "add \"a+bi\"" + endc + " - adds the complex number to the list")
    print(
        green + "insert \"a+bi\" at \"x\"" + endc + "- inserts the complex number at position x (positions are "
                                                    "numbered "
                                                    " starting from 0)\n")

    print(red + "remove \"x\"" + endc + " - removes the number at position x from the list")
    print(red + "remove \"x\" to \"y\"" + endc + " - removes the numbers from position x to position y"
                                                 " (including the numbers situated on position x and y)\n")

    print(blue + "replace \"a+bi\" with \"c+di\"" + endc + " - replaces all occurrences of a+bi with c+di\n")

    print(yellow + "list " + endc + "- displays the list of numbers")
    print(yellow + "list real \"x\" to \"y\"" + endc + " - display the real numbers (imaginary part = 0) beginning "
                                                       "at index x and ending at index y")
    print(
        yellow + "list modulo \"symbol\" \"x\"" + endc + " - (where symbol ∈ [ < , = , > ]) display all numbers having "
                                                         "modulus in a certain way (example: list modulo < 10, "
                                                         "list modulo = 5)\n")

    print(magenta + "sum \"x\" to \"y\"" + endc + " – display the sum of the numbers between positions x and y")
    print(magenta + "product \"x\" to \"y\"" + endc + " - display the product of numbers between positions x and y\n")

    print(cyan + "filter real" + endc + " – keep only numbers having imaginary part = 0")
    print(cyan + "filter modulo \"symbol\" \"x\"" + endc + " – (where symbol ∈ [ < , = , > ]) keep only numbers "
                                                           "having modulus in a certain way"
                                                           "compared to x\n")

    print(bblue + "undo" + endc + " – the last operation that modified program data is reversed. "
                                  "You can undo all operations performed since program start by repeatedly"
                                  " calling this function\n")

    print(red + bold + "exit" + endc)


def print_complex(nr):
    """Prints a complex number a user-friendly way"""
    realp = entity.get_realp(nr)
    imaginaryp = entity.get_imaginaryp(nr)

    imaginaryp_negative = 0

    if realp == 0:
        print(str(imaginaryp) + 'i')
        return

    if imaginaryp < 0:
        imaginaryp = -imaginaryp
        imaginaryp_negative = 1

    if imaginaryp == 0:
        print(realp)
        return

    elif imaginaryp_negative == 0:
        print(str(realp) + " + " + str(imaginaryp) + 'i')
    else:
        print(str(realp) + " - " + str(imaginaryp) + 'i')


def print_list(li_complex):
    for index in range(0, len(li_complex)):
        print(str(index + 1) + ".)", end=" ")
        print_complex(li_complex[index])


def print_sum(input_list, li_complex):
    print_complex(functions.pass_sum_complex(input_list, li_complex))


def print_product(input_list, li_complex):
    print_complex(functions.pass_product_complex(input_list, li_complex))


def start():
    """Control function"""

    print_menu()

    # Testing
    li_complex = []
    tests.test_init(li_complex)
    #

    cmds = ["add", "insert", "remove", "replace", "list", "sum", "product", "filter", "undo", "exit"]
    li_undo = []

    while 1:
        # Getting user input and formatting it

        input_str = input("\nWhat would you like to do?\n")
        input_list = functions.format_input(input_str)

        #

        # Calling functions for desired command

        command = input_list[0]

        if command not in cmds or len(input_list) > 5:
            print("The command you have typed does not belong to the list of "
                  "implemented commands.")

        elif command == "add":

            try:
                nr = functions.create_complex(input_list[1])

                li_copy = copy.deepcopy(li_complex)
                functions.add_complex(li_complex, nr)
                li_undo.append(li_copy)
                print("You have successfully added a complex number to the list.")
            except:
                print("The complex number you have typed is of incorrect form!")

        elif command == "insert":

            try:
                li_copy = copy.deepcopy(li_complex)
                index = functions.insert_complex(input_list, li_complex)
                li_undo.append(li_copy)

                print("You have successfully inserted your complex number at position " + str(index) + ".")
            except ValueError:
                print("The command you have entered is not of correct form!")
            except IndexError:
                print("The index you have typed is out of range!")

        elif command == "remove":
            try:
                nr_cmds = len(input_list)
                li_copy = copy.deepcopy(li_complex)
                do_remove(input_list, li_complex, nr_cmds)
                li_undo.append(li_copy)
            except ValueError:
                print("The indexes you have typed are of incorrect form!")
            except IndexError:
                print("The index you have typed is out of range!")

        elif command == "replace":

            try:
                li_copy = copy.deepcopy(li_complex)
                li_complex = functions.replace_complex(input_list, li_complex)
                li_undo.append(li_copy)
                print("You have successfully performed the operation!")
            except ValueError:
                print("The complex numbers you have typed are of incorrect form!")
            except IndexError:
                print("The complex number you want to replace does not exist in the list!")

        elif command == "list":

            nr_cmds = len(input_list)

            try:
                do_list(input_list, li_complex, nr_cmds)

            except ValueError:
                print("The command you have entered is of incorrect form!")
            except IndexError:
                print("The indexes you have typed are out of range!")

        elif command == "sum":  # sum
            try:
                print_sum(input_list, li_complex)

            except ValueError:
                print("The command you have entered is of incorrect form!")
            except IndexError:
                print("The indexes you have typed are out of range!")

        elif command == "product":  # product
            try:
                print_product(input_list, li_complex)

            except ValueError:
                print("The command you have entered is of incorrect form!")
            except IndexError:
                print("The indexes you have typed are out of range!")

        elif command == "filter":  # filter
            try:
                li_copy = copy.deepcopy(li_complex)
                li_complex = do_filter(input_list, li_complex)
                li_undo.append(li_copy)
                print("You have successfully filtered the list.")
            except ValueError:
                print("The command you have entered is of incorrect form!")

        elif command == "undo":  # undo
            try:
                li_complex, li_undo = functions.undo(li_undo)
                print("You have successfully undone the last operation.")
            except ValueError as ve:
                print(ve)

        elif command == "exit":
            return

    #


def do_filter(input_list, li_complex):
    nr_commands = len(input_list)

    if nr_commands == 1:
        raise ValueError

    if input_list[1] == "real":
        li_complex = functions.filter_real(li_complex)
        return li_complex
    elif input_list[1] == "modulo":
        if nr_commands != 4:
            raise ValueError

        sgn = input_list[2]

        if not sgn in ['<', '=', '>']:
            raise ValueError

        return functions.filter_modulo(input_list, li_complex)
    else:
        raise ValueError
