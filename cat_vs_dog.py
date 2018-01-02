#!/bin/python

'''
@joseanavarrete

Cat vs Dog Spotify puzzle

https://labs.spotify.com/puzzles/
'''

import unittest


class CatVsDogContest(object):
    def __init__(self, n_cats, n_dogs, votes):
        self.votes = self._init_votes(n_cats, n_dogs)
        for stay, leave in votes:
            self.votes[stay] += 1
    
    def max_num_satisfied_voters(self):
        ''' Gets the max upvotes number '''
        return str(max(self.votes.values()))

    def _init_votes(self, n_cats, n_dogs):
        cats = list(map(lambda x: 'C' + str(x), range(1, n_cats+1)))
        dogs = list(map(lambda x: 'D' + str(x), range(1, n_dogs+1)))
        initial_votes = [0] * (n_cats+n_dogs)
        return dict(zip(cats+dogs, initial_votes))

class TestCatVsDogContest(unittest.TestCase):
    def setUp(self):
        '''Init expected_output and contest list based on given data _data'''
        self.expected_output = """1
3
3"""
        _data = """3
1 1 2
C1 D1
D1 C1
1 2 4
C1 D1
C1 D1
C1 D2
D2 C1
2 2 6
C1 D1
D1 C2
D1 C1
D2 C2
C1 D2
D1 C1"""

        data_lines = _data.splitlines()
        n_test_cases = int(data_lines[0])
        n_configs = 0
        config_case_position = 1
        self.contest_cases = []

        while n_configs < n_test_cases:
            n_cats, n_dogs, n_voters = tuple(
                map(int, data_lines[config_case_position].split(' ')))
            votes = [
                tuple(l.split(' '))
                for l in data_lines[config_case_position+1:config_case_position+n_voters+1]
            ]
            contest = CatVsDogContest(n_cats, n_dogs, votes)
            self.contest_cases.append(contest)
            n_configs += 1
            config_case_position += n_voters+1

    def test_max_num_satisfied_voters(self):
        '''
        Creates a list of satisfied voters per test case and
        joins it in a multiline string
        '''
        max_num_satisfied_voters = []
        for contest in self.contest_cases:
            max_num_satisfied_voters.append(contest.max_num_satisfied_voters())

        self.assertEqual('\n'.join(max_num_satisfied_voters),
                         self.expected_output)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
