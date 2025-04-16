"""
Chapter 4 - Primitive Types

- everything is an object in python
- integers are unbounded which means the maximum integer representable is
  dependent on the memory
- negative numbers are treated as their 2's complement value (no unsigned
  shifts)
###############################################################################
- XOR (^):
    - copy and pasted from: https://stackoverflow.com/questions/14526584/what-does-the-xor-operator-do

    "XOR is a binary operation, it stands for "exclusive or", that is to say the resulting bit evaluates to one if only exactly one of the bits is set.
    This is its function table:

    a | b | a ^ b
    --|---|------
    0 | 0 | 0
    0 | 1 | 1
    1 | 0 | 1
    1 | 1 | 0
    This operation is performed between every two corresponding bits of a number.

    Example: 7 ^ 10
    In binary: 0111 ^ 1010

      0111
    ^ 1010
    ======
      1101 = 13
    Properties: The operation is commutative, associative and self-inverse.

    It is also the same as addition modulo 2."
###############################################################################
"""


# https://en.wikipedia.org/wiki/Parity_bit
# O(N) time, O(1) space; N - word size
# checks the parity of a binary word - 1 if number of 1s is odd, otherwise 0
# brute force - iteratively test the value of each bit while tracking the
# number of 1s seen so far
def parity_bf(x):
    result = 0
    print("result: ", result, " x: ", x)
    while x:
        result ^= x & 1  # store the number mod 2
        x >>= 1
        print("result: ", result, " x: ", x)
    return result


# count the number of bits that are set to 1 in a positive integer
# this tests bits one at a time starting with the least-significant bit
# this algorithms runs in O(N) time and O(1) space
def count_bits(x):
    num_bits = 0
    print("num_bits: ", num_bits, " x: ", x)
    while x:
        num_bits += x & 1  # this checks if the least-significant bit is set
        x >>= 1  # right shifts the bits by one
        print("num_bits: ", num_bits, " x: ", x)
    return num_bits


def bit_wise_operators():
    print("6 & 4: ", 6 & 4)
    print("1 | 2: ", 1 | 2)
    print("8 >> 1: ", 8 >> 1)
    print("-16 >> 2: ", -16 >> 2)
    print("1 << 10: ", 1 << 10)
    print("~0: ", ~0)
    print("15 ^ 32: ", 15 ^ 32)


def main():
    # print(count_bits(24343))
    bit_wise_operators()
    parity_bf(23432429)
    parity_bf(34)


if __name__ == "__main__":
    main()
