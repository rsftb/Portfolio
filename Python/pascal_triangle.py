"""
This script prints out any row of Pascal's Triangle using the binomial coefficient function.
Row indices are zero-indexed, for example:
 >>> rowIndex(4) #// 5th row
 >>> [1, 4, 6, 4, 1]
"""


def factorial(n:int) -> int:
    "Computes the product of all positive integers from 0 up to a given number (5! = 120)"

    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


def C(n:int, k:int) -> int:
    """
    Binomial coefficient function\n
    `n` is the size of the set\n
    `k` is the number of items picked from the set\n
    `C(8, 5) = 56` means there are 56 different ways to group any 5 items out of a set of 8 items
    """

    nf, kf = factorial(n), factorial(k)

    nkf = factorial(n - k)

    coefficient = nf // (kf * nkf)

    return coefficient

print(C(4, 2))


def pascals_triangle_row(n:int) -> list:
    "Returns a row from Pascal's Triangle by index. Starts from zero."
    row = []

    for k in range(n+1):
        coefficient = C(n, k)
        row.append(coefficient)

    return row

print(pascals_triangle_row(4))
print(pascals_triangle_row(5))

"""
       1    -0
      1 1    -1
     1 2 1    -2
    1 3 3 1    -3
   1 4 6 4 1    -4
 1 5 10 10 5 1   -5
"""
