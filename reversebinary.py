#!/bin/python
"""
reversebinary puzzle for Spotify.com

v1

Jose Antonio Navarrete

You can find me at janavarretecristino@gmail.com
Follow me on twitter @joseanavarrete
"""

import unittest

MAX_VALUE = 1000000000

def reverse_binary(n):
    """
    Receives an integer (n), converts it to its reverse binary
    """
    if not 1 <= n <= MAX_VALUE:
        raise ValueError
    
    binary_str = bin(n)  # '0bXXXX' where XXXX is n in binary
    return int(binary_str[::-1][:-2], 2)


class ReverseBinaryTest(unittest.TestCase):
    def test_reverse_binary(self):
        self.assertEqual(reverse_binary(1), 1)
        self.assertEqual(reverse_binary(13), 11)
        self.assertEqual(reverse_binary(47), 61)

    def test_wrong_input(self):
        with self.assertRaises(ValueError):
            reverse_binary(0)
            reverse_binary(MAX_VALUE)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
