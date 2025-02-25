#!/usr/bin/env python3

import sys
from decimal import Decimal


# Student ID: 3367315


#  *** Note: This should be set to 15 in your submitted code.
#
# You will want to set it to 15 when running against the large ratings.txt data file.
# You will want to set it to 1 or 2 when running against the smaller r5.txt and r100.txt files
# otherwise films with small numbers of votes will be prevented from producing results.
min_votes = 1
print('min_votes = %s' % min_votes, file=sys.stderr)


# Note: The code below does not solve the problem that you have been
# given (nor does it use min_votes) but it should help you see
# the keys and values the reducer is receiving, and their ordering.
# You will need to make significant changes to this code to
# implement a solution that produces the correct output.


# You may want to write:
#     * code that filters based on min_votes,
#     * code that averages,
#     * code that finds the highest(s).
#   ...these are just suggestions/hints.


rating_count = 0
genre = None
movie = None

# Process the input line by line.
for line in sys.stdin:

    title, genre, year, rating = line.strip().split('\t')

    """
    Movies have one year but they can have multiple genres.
    We accumulate the ratings of each movie for each genre
    """

    print(line.strip())
