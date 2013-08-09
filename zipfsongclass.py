#!/usr/bin/python2

"""
Zifpsong with class version
"""

import sys

class Song:
    """Song which contains zipf, name and position"""
    def __init__(self, zipf, name, position):
        self.zipf = zipf
        self.name = name
        self.position = position


    def zipf_index(self):
        return self.zipf


    def position_index(self):
        return self.position


    def get_name(self):
        return self.name


def my_reverse_multi_sort(x, y):
    """"
    Reverse order for zipf and song position sorting
    """
    n_cmp = cmp(y.zipf_index(), x.zipf_index())
    if n_cmp == 0:
        return cmp(x.position_index(), y.position_index())
    else:
        return n_cmp


def main():
    song_list = []
    options = map(int, sys.stdin.readline().split())
    for i in xrange(options[0]):
        song_attr = map(lambda s: s.strip(), sys.stdin.readline().split())
        song_list.append(Song((i+1.0)*int(song_attr[0]), song_attr[1], i+1.0))
    return_list = sorted(song_list, cmp=my_reverse_multi_sort)[:options[1]]
    print "\n".join([s.get_name() for s in return_list])


if __name__ == '__main__':
    main()