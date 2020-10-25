# Test functions go here
#
# Test functions:
#   - no print / input
#   - great friends with assert

# Imports

import functions.functions as functions
import domain.entity as entity
import copy

#

def test_init(li_complex):
    # use this function to add the 10 required items
    # use it to set up test data

    li_append(li_complex)

    # Add
    test_add(li_complex)
    #

    # Insert
    test_insert(li_complex)
    #

    # Remove single
    test_remove_single(li_complex)
    #

    # Remove multiple
    test_remove_multiple(li_complex)
    #

    # Replace
    test_replace(li_complex)
    #

    # Sum
    test_sum_complex(li_complex)
    #

    # Product
    test_product_complex(li_complex)
    #

    # Filter Real
    test_filter_real(li_complex)
    #

    # Filter Modulo
    test_filter_modulo(li_complex)
    #

    # Undo
    test_undo()
    #


def test_replace(li_complex):
    assert li_complex[5] == [10, 0]
    li_complex = functions.replace_complex(["replace", "10+0i", "with", "12+0i"], li_complex)
    assert li_complex[5] == [12, 0]


def test_remove_multiple(li_complex):
    functions.add_complex(li_complex, [1, 1])
    functions.add_complex(li_complex, [1, 1])
    functions.add_complex(li_complex, [1, 1])
    functions.remove_multiple(["remove", 11, "to", 13], li_complex)
    assert len(li_complex) == 10


def test_remove_single(li_complex):
    functions.remove_single(["remove", 3], li_complex)
    assert len(li_complex) == 10


def test_insert(li_complex):
    functions.insert_complex(["insert", "1+200i", "at", "3"], li_complex)
    assert li_complex[2] == [1, 200]
    assert len(li_complex) == 11


def test_add(li_complex):
    functions.add_complex(li_complex, [2, -7])
    assert len(li_complex) == 10


def test_sum_complex(li_complex):
    s = functions.sum_complex(1, 3, li_complex)
    assert s == [1, -5]

    s = functions.sum_complex(6, 9, li_complex)
    assert s == [8, 2]

    s = functions.sum_complex(1, 4, li_complex)
    assert s == [-14, 15]


def test_product_complex(li_complex):
    p = functions.product_complex(1, 3, li_complex)
    assert p == [10, 80]

    p = functions.product_complex(6, 7, li_complex)
    assert p == [-60, 30]

    p = functions.product_complex(4, 5, li_complex)
    assert p == [1320, 4740]

    p = functions.product_complex(4, 4, li_complex)
    assert p == [-15, 20]


def test_filter_real(li_complex):
    li_complex = functions.filter_real(li_complex)
    assert (entity.get_imaginaryp(nr_complex) == 0 for nr_complex in li_complex)


def test_filter_modulo(li_complex):
    li_complex = functions.filter_modulo_smaller(15, li_complex)
    assert (functions.complex_modulus(nr_complex) >= 15 for nr_complex in li_complex)

    li_append(li_complex)

    li_complex = functions.filter_modulo_equal(10, li_complex)
    assert (functions.complex_modulus(nr_complex) == 10 for nr_complex in li_complex)

    li_append(li_complex)

    li_complex = functions.filter_modulo_greater(15, li_complex)
    assert (functions.complex_modulus(nr_complex) <= 15 for nr_complex in li_complex)


def test_undo():
    li_test = []
    li_append(li_test)
    length = len(li_test)
    li_undo = ['']
    li_copy = copy.deepcopy(li_test)
    li_undo.append(li_copy)
    functions.remove_multiple(['remove', '1', 'to', '3'], li_test)
    assert not length == len(li_test)
    li_complex, li_undo = functions.undo(li_undo)
    assert length == len(li_complex)


def li_append(li_complex):
    li_complex.append([2, 3])
    li_complex.append([-1, 2])
    li_complex.append([0, -10])
    li_complex.append([-15, 20])
    li_complex.append([120, -156])
    li_complex.append([10, 0])
    li_complex.append([-6, 3])
    li_complex.append([9, 1])
    li_complex.append([-5, -2])
