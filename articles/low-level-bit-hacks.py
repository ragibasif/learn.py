# https://catonmat.net/low-level-bit-hacks
# bit enumerations start with 0
# (2 ** n) -1 : the formula for getting the largest unsigned integer that can
# be represented with n bits
"""
Truth table for AND, OR, XOR
a | b | a AND b
---------------
0 | 0 | 0
0 | 1 | 0
1 | 0 | 0
1 | 1 | 1
a | b | a OR b
--------------
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 1
a | b | a XOR b
---------------
0 | 0 | 0
0 | 1 | 1
1 | 0 | 1
1 | 1 | 0
"""


def even_or_odd(self, x=0):
    # check if even or odd
    # an integer is odd iff the least significant bit is 1
    # by AND-ing an integer with 1, all other bits get eliminated
    """
        00101011
    &   00000001   (note: 1 is the same as 00000001)
        --------
        00000001
    """
    # two's complement notation - to find the negative of a number in 2's
    # complement notation, invert all the bits and add one
    # -43 is 11010101 in binary
    # 98 in binaray is 1100010, after AND-ing with 1, the result is 0
    """
        01100010
    &   00000001
        --------
        00000000
    """
    # print 0 for even
    # print 1 for odd
    print("x", x)
    print(x & 1)
    if (x & 1) == 0:
        print(x, "is even")
    else:
        print(x, "is odd")


def is_nth_bit_set(x, n):
    # (x & 1) - tests if the first bit is set (least significant bit)
    # x & (1 << n) - tests if the nth bit is set by shifting that first 1 bit n
    # positions to the left and then doing the same AND operation, this gets
    # rid of all bits except the nth bit
    """
    viz of what happens when you shift 1 several positions to the left
    1         00000001    (same as 1<<0)
    1<<1      00000010
    1<<2      00000100
    1<<3      00001000
    1<<4      00010000
    1<<5      00100000
    1<<6      01000000
    1<<7      10000000
    """
    """
    122 & (1<<3)
        01111010
    &   00001000
        --------
        00001000
    """
    """
        11011111      (-33 in binary)
    &   00100000     (1<<5)
        --------
        00000000
    """
    print("x", x)
    print("n", n)
    if x & (1 << n):
        print(n, "th bit is set")
    else:
        print(n, "th bit is not set")


def set_nth_bit(x, n):
    # sets nth bit by shifting the 1 n times (1<<n) with the OR op
    # OR-ing anything with 0, leaves the original as is
    # OR-ing anything with 1, turns the original to 1 if it wasnt already
    """
    setting the 2nd bit on 120:
        01111000    (120 in binary)
    |   00000100    (1<<2)
        --------
        01111100
    """
    """
    -120 and 6th bit
        10001000   (-120 in binary)
    |   01000000   (1<<6)
        --------
        11001000
    """
    y = x | (1 << n)
    print("x: ", x, " y: ", y, " n: ", n)


def unset_nth_bit(x, n):
    # ~(1<<n) - turns on all the bits except the n-th
    # AND-ing the variable 'x' with this quantity means you are eliminating the
    # nth-bit because AND-ing anythin with 0 sets it to 0 regardless of what
    # the value was before
    """
    ~1        11111110  (same as ~(1<<0))
    ~(1<<1)   11111101
    ~(1<<2)   11111011
    ~(1<<3)   11110111
    ~(1<<4)   11101111
    ~(1<<5)   11011111
    ~(1<<6)   10111111
    ~(1<<7)   01111111
    """
    """
    unset the 4th bit in 127
        01111111    (127 in binary)
    &   11101111    (~(1<<4))
        --------
        01101111
    """
    y = x & ~(1 << n)
    print("x: ", x, " y: ", y, " n: ", n)


def circular_shift(x, n):
    len_of_bin_str = 2**n
    y = (x << n) | (x >> (len_of_bin_str - n))
    print("x << n", x << n)
    print("x >> (len_of_bin_str - n)", x >> (len_of_bin_str - n))
    print("x: ", x, " y: ", y, " n: ", n)


def toggle_nth_bit(x, n):
    # XOR-ing two bits that are the same will result in 0, and if the two bits
    # are different it will result in 1
    # 0 ^ 0 = 0
    # 1 ^ 1 = 0
    # 0 ^ 1 = 1
    # 1 ^ 0 = 1
    """
    toggle the 5th bit when its 1
        01110101
    ^   00100000
        --------
        01010101

    toggle the 5th bit when its 0
        01010101
    ^   00100000
        --------
        01110101
    """
    # XOR-ing the same bit twice returns its original value
    # useful for calculating parity
    y = x ^ (1 << n)
    print("x: ", x, " y: ", y, " n: ", n)


def turn_off_rightmost_bit(x):
    # turns off the rightmost one-bit
    # 00101010 -> 00101000
    # 00010000 -> 00000000
    """
    unsigned integers:

        01010111    (x)
    &   01010110    (x-1)
        --------
        01010110

        01011000    (x)
    &   01010111    (x-1)
        --------
        01010000

        10000000    (x = -128)
    &   01111111    (x-1 = 127 (with overflow))
        --------
        00000000

        11111111    (x = all bits 1)
    &   11111110    (x-1)
        --------
        11111110

        00000000    (x = no rightmost 1-bits)
    &   11111111    (x-1)
        --------
        00000000
    """
    # two possible scenarios:
    y = x & (x - 1)
    print("x: ", x, " y: ", y)


def isolate_rightmost_one_bit(x):
    # finds the rightmost 1 bit and sets all the other bits to 0 with two's
    # complement (only works because of two's complement)
    # two's complement systems: x == (~x + 1)
    """
        10111100  (x)
    &   01000100  (-x)
        --------
        00000100

        01110000  (x)
    &   10010000  (-x)
        --------
        00010000

        00000001  (x)
    &   11111111  (-x)
        --------
        00000001

        10000000  (x = -128)
    &   10000000  (-x = -128)
        --------
        10000000

        11111111  (x = all bits one)
    &   00000001  (-x)
        --------
        00000001

        00000000  (x = all bits 0, no rightmost 1-bit)
    &   00000000  (-x)
        --------
        00000000
    """
    y = x & (-x)
    print("x: ", x, " y: ", y)


def right_propagate_rightmost_one_bit(x):
    # all the 0-bits to the rightmost 1-bit gets turned into ones
    # 01010000 -> 01011111
    # WARNING: if x = 0, it produces all 1s
    """
        10111100  (x)
    |   10111011  (x-1)
        --------
        10111111

        01110111  (x)
    |   01110110  (x-1)
        --------
        01110111

        00000001  (x)
    |   00000000  (x-1)
        --------
        00000001

        10000000  (x = -128)
    |   01111111  (x-1 = 127)
        --------
        11111111

        11111111  (x = -1)
    |   11111110  (x-1 = -2)
        --------
        11111111

        00000000  (x)
    |   11111111  (x-1)
        --------
        11111111
    """
    y = x | (x - 1)
    print("x: ", x, " y: ", y)


def isolate_the_rightmost_zero_bit(x):
    """
        10111100  (x)
        --------
        01000011  (~x)
    &   10111101  (x+1)
        --------
        00000001

        01110111  (x)
        --------
        10001000  (~x)
    &   01111000  (x+1)
        --------
        00001000

        00000001  (x)
        --------
        11111110  (~x)
    &   00000010  (x+1)
        --------
        00000010

        10000000  (x = -128)
        --------
        01111111  (~x)
    &   10000001  (x+1)
        --------
        00000001

        11111111  (x = no rightmost 0-bit)
        --------
        00000000  (~x)
    &   00000000  (x+1)
        --------
        00000000

        00000000  (x)
        --------
        11111111  (~x)
    &   00000001  (x+1)
        --------
        00000001
    """
    # find the rightmost zero bit by turning all other bits to 0 and setting
    # the rightmost zero bit to 1 in the result
    y = ~x & (x + 1)
    print("x: ", x, " y: ", y)


def turn_on_the_rightmost_zero_bit(x):
    # change the rightmost zero bit into 1
    """
        10111100  (x)
    |   10111101  (x+1)
        --------
        10111101

        01110111  (x)
    |   01111000  (x+1)
        --------
        01111111

        00000001  (x)
    |   00000010  (x+1)
        --------
        00000011

        10000000  (x = -128)
    |   10000001  (x+1)
        --------
        10000001

        11111111  (x = no rightmost 0-bit)
    |   00000000  (x+1)
        --------
        11111111

        00000000  (x)
    |   00000001  (x+1)
        --------
        00000001
    """
    # OR-ing x with x+1 loses no information and adds 1 to the first rightmost
    # 0 if it exists. If there was no rightmost 0, then (x+1) overflows and
    # becomes all 0s which when OR-ed with x just gives back x
    y = x | (x + 1)
    print("x: ", x, " y: ", y)


def int_to_bin(num, bits=8):
    r = ""
    while bits:
        r = ("1" if num & 1 else "0") + r
        bits = bits - 1
        num = num >> 1
    print(r)


def main():
    x = -43
    y = 98
    n = 3
    print("x: ", x, " y: ", y, " n: ", n)
    int_to_bin(x, n)
    int_to_bin(y, n)
    int_to_bin(x)
    int_to_bin(y)
    int_to_bin(1023)


main()
