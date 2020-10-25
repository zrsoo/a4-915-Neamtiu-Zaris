"""
Functions that implement program features. They should call each other, or other functions from the domain
"""

# Imports

import domain.entity as entity
import math
import copy

#


def create_complex(str_complex):
    """
    Transforms the string "a + bi" into a storage-friendly object
    :param str_complex: "a + bi", where a and b are integers
    :return: A list containing the real and imaginary part of the complex number
    """

    if len(str_complex) < 4:
        raise ValueError

    # Removing the "i".
    str_complex = str_complex.strip("i")

    # If there is a minus on the first position, then the real part is negative
    if str_complex[0] == '-':
        realp_negative = 1
    else:
        realp_negative = 0

    # If there is a minus beyond position 1, then we know
    # for sure that the imaginary part is negative, we
    # need this in order to know if we are going to use "+"
    # or "-" when splitting.
    if '-' in str_complex[1:]:
        imagp_negative = 1
    else:
        imagp_negative = 0

    if imagp_negative == 1:
        nr = str_complex.split("-")
    else:
        nr = str_complex.split("+")

    nr_complex = [''] * 2

    if realp_negative and imagp_negative:
        nr.remove('')
        entity.set_realp(nr_complex, -int(nr[0]))
    else:
        entity.set_realp(nr_complex, nr[0])

    if imagp_negative == 1:
        entity.set_imaginaryp(nr_complex, -int(nr[1]))  # If the imaginary part is negative, we set it as such.
    else:
        entity.set_imaginaryp(nr_complex, nr[1])

    return nr_complex


def format_input(input_str):
    """
    Using the input string, builds a list containing the user command
    and the arguments of the command
    :param input_str: The string that the user typed
    :return: A list containing the command and its arguments
    """

    cmd_list = input_str.split()
    return cmd_list


def add_complex(li_complex, nr):
    li_complex.append(nr)


def complex_modulus(nr_complex):
    realp = entity.get_realp(nr_complex)
    imaginaryp = entity.get_imaginaryp(nr_complex)

    modulus = math.sqrt(realp * realp + imaginaryp * imaginaryp)

    return modulus


def replace_complex(input_list, li_complex):
    complex_tbr = create_complex(input_list[1])
    complex_rpm = create_complex(input_list[3])
    if complex_tbr not in li_complex:
        raise IndexError
    li_complex = [element if element != complex_tbr else complex_rpm for element in li_complex]
    return li_complex


def remove_multiple(input_list, li_complex):
    sindex = int(input_list[1])
    eindex = int(input_list[3])
    nrpops = eindex - sindex + 1

    if sindex > eindex or sindex < 0 or eindex > len(li_complex):
        raise ValueError

    for index in range(0, nrpops):
        li_complex.pop(sindex - 1)

    return eindex, sindex


def remove_single(input_list, li_complex):
    index = int(input_list[1])
    li_complex.pop(index - 1)
    return index


def insert_complex(input_list, li_complex):
    nr = create_complex(input_list[1])

    index = int(input_list[3])

    if input_list[2] != "at":
        raise ValueError
    if index < 0 or index > len(li_complex) + 1:
        raise IndexError
    li_complex.insert(index - 1, nr)

    return index


# Sum


def pass_sum_complex(input_list, li_complex):
    start_index = int(input_list[1])  # The index from where the summing begins
    end_index = int(input_list[3])  # The index where the summing ends

    if not input_list[2] == "to":
        raise ValueError

    sum = sum_complex(start_index, end_index, li_complex)

    return sum


def sum_complex(start_index, end_index, li_complex):
    start_index -= 1
    end_index -= 1

    if start_index < 0 or end_index >= len(li_complex):
        raise IndexError("The indexes you have typed are out of range!")

    realp_sum = 0
    imaginaryp_sum = 0

    complex_sum = [''] * 2

    for index in range(start_index, end_index + 1):
        realp_sum += entity.get_realp(li_complex[index])
        imaginaryp_sum += entity.get_imaginaryp(li_complex[index])

    entity.set_realp(complex_sum, realp_sum)
    entity.set_imaginaryp(complex_sum, imaginaryp_sum)

    return complex_sum


# Product


def pass_product_complex(input_list, li_complex):
    start_index = int(input_list[1])  # The index from where the summing begins
    end_index = int(input_list[3])  # The index where the summing ends

    if not input_list[2] == "to":
        raise ValueError

    prod = product_complex(start_index, end_index, li_complex)

    return prod


def product_complex(start_index, end_index, li_complex):
    start_index -= 1
    end_index -= 1

    if start_index < 0 or end_index >= len(li_complex):
        raise IndexError("The indexes you have typed are out of range!")

    realp_prod = 1
    imaginaryp_prod = 1

    complex_prod = [''] * 2

    realp_prod = entity.get_realp(li_complex[start_index])
    imaginaryp_prod = entity.get_imaginaryp(li_complex[start_index])

    for index in range(start_index + 1, end_index + 1):
        real_current = realp_prod
        imaginary_current = imaginaryp_prod

        real_next = entity.get_realp(li_complex[index])
        imaginary_next = entity.get_imaginaryp(li_complex[index])

        realp_prod = real_current * real_next - imaginary_current * imaginary_next
        imaginaryp_prod = real_current * imaginary_next + real_next * imaginary_current

    entity.set_realp(complex_prod, realp_prod)
    entity.set_imaginaryp(complex_prod, imaginaryp_prod)

    return complex_prod


# Filter

def filter_real(li_complex):
    return list(filter(lambda nr_complex: (entity.get_imaginaryp(nr_complex) == 0), li_complex))


def filter_modulo(input_list, li_complex):
    sgn = input_list[2]
    nr = int(input_list[3])

    if sgn == '>':
        li_new = filter_modulo_greater(nr, li_complex)
    elif sgn == '=':
        li_new = filter_modulo_equal(nr, li_complex)
    elif sgn == '<':
        li_new = filter_modulo_smaller(nr, li_complex)

    return li_new


def filter_modulo_greater(nr, li_complex):
    return list(filter(lambda nr_complex: (complex_modulus(nr_complex) > nr), li_complex))


def filter_modulo_equal(nr, li_complex):
    return list(filter(lambda nr_complex: (complex_modulus(nr_complex) == nr), li_complex))


def filter_modulo_smaller(nr, li_complex):
    return list(filter(lambda nr_complex: (complex_modulus(nr_complex) < nr), li_complex))


# Undo

def undo(li_undo):
    length = len(li_undo)

    if length == 0:
        raise ValueError("The list hasn't had any changes performed yet or you undid them all.")

    li_new = copy.deepcopy(li_undo[length - 1])
    li_undo.pop()

    return li_new, li_undo
