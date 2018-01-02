#!/usr/bin/python2

""""
Zipf's song problem
v1.0 without using any class structure like creating a Song class
Jose Antonio Navarrete
@joseanavarrete
"""

import sys


def process_info(n_played, song_name, song_number, songs_array):
    """
    Inserts into songs_array song_name processed with its zipf coeficient
    """
    zipf = n_played*song_number
    song = {'zipf': zipf, 'name': song_name, 'song_number': song_number}
    songs_array.append(song)


def my_reverse_multi_sort(x, y):
    """"
    Reverse order for zipf and song_number sorting
    """
    n_cmp = cmp(y['zipf'], x['zipf'])
    if n_cmp == 0:
        return cmp(x['song_number'], y['song_number'])
    else:
        return n_cmp


def sort_and_print_list(songs_array, max_length):
    returning_list = sorted(songs_array, cmp=my_reverse_multi_sort)[:max_length]
    print "\n".join([s['name'] for s in returning_list])


def main():
    songs_array = []
    options = map(int, sys.stdin.readline().split())
    for x in xrange(options[0]):
        spl_line = map(lambda s: s.strip(), sys.stdin.readline().split())
        process_info(long(spl_line[0]), spl_line[1], x+1.0, songs_array)
    sort_and_print_list(songs_array, options[1])


if __name__ == '__main__':
    main()
