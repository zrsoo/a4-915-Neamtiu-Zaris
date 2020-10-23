"""
Domain file includes code for entity management
entity = number, transaction, expense etc.
"""


#
# domain section is here (domain = numbers, transactions, expenses, etc.)
# getters / setters
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)


def get_realp(nr):
    return nr[0]


def get_imaginaryp(nr):
    return nr[1]


def set_realp(nr, realp):
    nr[0] = int(realp)


def set_imaginaryp(nr, imaginaryp):
    nr[1] = int(imaginaryp)