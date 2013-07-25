#!/usr/bin/python2
"""
reversebinary puzzle for Spotify.com

v1

Jose Antonio Navarrete

You can find me at janavarretecristino@gmail.com
Follow me on twitter @joseanavarrete
"""

import sys


def reverseBinary(n):
    """
    Receives an integer (n), converts it to its reverse binary
    E.g reverseBinary(13) returns 11 because the reverse of 1101 is 1011
    """
    binary_str = bin(n)  # '0bXXXX' where XXXX is n in binary
    reverse_str = binary_str[::-1][:-2]  # we do not want '0b' characters

    # It could have been done in one line but I want you to know I know what
    # I am doing. One line version:
    # print int(bin(n)[::-1][:-2], 2)
    print int(reverse_str, 2)


def main():
    try:
        for number in sys.stdin:
            n = int(number)
            if 1 <= n <= 1000000000:
                reverseBinary(n)
            else:
                raise ValueError
    except ValueError:
        print "Usage error. Please enter only values between 1 and 10E9"

if __name__ == '__main__':
    main()
