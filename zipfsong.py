#!/bin/python

"""
Zifpsong

https://labs.spotify.com/puzzles/
"""

import unittest

class Song(object):
    """Song which contains zipf, name and position"""
    def __init__(self, n_plays, name, position):
        self.zipf_quality = position*n_plays
        self.name = name
        self.position = position

class Album(object):
    def __init__(self, songs, max_zipfy_songs):
        self.songs = songs
        self.max_zipfy_songs = max_zipfy_songs
    
    @classmethod
    def from_multiline_str(cls, options):
        """
        Options is a multiline string like:
        total_songs zipfy_songs
        n_plays song_name
        n_plays song_name
        n_plays song_name
        """
        options_list = options.split('\n')
        total_songs, max_zipfy_songs = map(int, options_list[0].split())
        album_songs = []

        for song_index in range(1, total_songs+1):
            n_plays, song_name = options_list[song_index].split()
            album_songs.append(Song(int(n_plays), song_name, song_index))

        return cls(album_songs, max_zipfy_songs)

    def zipfy(self):
        zipfied_songs = sorted(
            self.songs,
            key=lambda song: song.zipf_quality,
            reverse=True)[:self.max_zipfy_songs]

        return "\n".join([song.name for song in zipfied_songs])


class AlbumZipfyTest(unittest.TestCase):
    def test_zipfy(self):
        test_album_1 = """4 2
30 one
30 two
15 three
25 four"""
        test_album_2 = """15 3
197812 re_hash
78906 5_4
189518 tomorrow_comes_today
39453 new_genious
210492 clint_eastwood
26302 man_research
22544 punk
19727 sound_check
17535 double_bass
18782 rock_the_house
198189 19_2000
13151 latin_simone
12139 starshine
11272 slow_country
10521 m1_a1"""

        expected_output_1 = """four
two"""
        expected_output_2 = """19_2000
clint_eastwood
tomorrow_comes_today"""

        album_1 = Album.from_multiline_str(test_album_1)
        album_2 = Album.from_multiline_str(test_album_2)

        self.assertEqual(album_1.zipfy(), expected_output_1)
        self.assertEqual(album_2.zipfy(), expected_output_2)

def main():
    unittest.main()


if __name__ == '__main__':
    main()
