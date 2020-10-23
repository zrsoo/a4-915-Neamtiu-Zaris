"""
This is the user interface module. These functions call functions from the domain and functions module.
"""

# Imports


#

# UI section
# (all functions that have input or print statements, or that CALL functions with print / input are  here).
# Ideally, this section should not contain any calculations relevant to program functionalities


def print_menu():
    """Prints the user menu"""

    print(bold + underlined + "\nList of commands:", endc + "\n")
    print(green + "add \"a+bi\"" + endc + " - adds the complex number to the list")
    print(
        green + "insert \"a+bi\" at \"x\"" + endc + " - inserts the complex number at position x (positions are numbered"
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
                                                         "modulo in a certain way (example: list modulo < 10, list modulo = 5)\n")
    print(red + bold + "exit" + endc)


def print_complex(nr):
    """Prints a complex number a user-friendly way"""
    realp = get_realp(nr)
    imaginaryp = get_imaginaryp(nr)

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


def start():
    """Control function"""

    print_menu()

    # Testing
    li_complex = []
    test_init(li_complex)
    #

    cmds = ["add", "insert", "remove", "replace", "list", "exit"]

    while (1):
        # Getting user input and formatting it

        input_str = input("\nWhat would you like to do?\n")
        input_list = format_input(input_str)

        #

        # Calling functions for desired command

        command = input_list[0]

        if command not in cmds or len(input_list) > 5:
            print("The command you have typed does not belong to the list of "
                  "implemented commands.")

        elif command == "add":

            try:
                nr = create_complex(input_list[1])
                add_complex(li_complex, nr)

                print("You have successfully added a complex number to the list.")
            except:
                print("The complex number you have typed is of incorrect form!")

        elif command == "insert":

            try:
                index = insert_complex(input_list, li_complex)

                print("You have successfully inserted your complex number at position " + str(index) + ".")
            except ValueError:
                print("The command you have entered is not of correct form!")
            except IndexError:
                print("The index you have typed is out of range!")

        elif command == "remove":
            try:
                nr_cmds = len(input_list)

                do_remove(input_list, li_complex, nr_cmds)
            except ValueError:
                print("The indexes you have typed are of incorrect form!")
            except IndexError:
                print("The index you have typed is out of range!")

        elif command == "replace":

            try:
                li_complex = replace_complex(input_list, li_complex)

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
                print("The command you have entered is not of correct form!")
            except IndexError:
                print("The indexes you have typed are out of range!")

        elif command == "exit":
            return

    #