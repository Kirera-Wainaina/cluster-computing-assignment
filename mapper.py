#!/usr/bin/env python3

import sys


# Student ID: 3367315


"""
The problem is to analyse a list of movie review ratings to find the film title(s) with the highest average rating for
each genre, for a specified set of years and genres.
"""

# Read included years.
with open('years.txt', 'r') as f:
    included_years = f.read().split()
    # Print debug/info message to stderr
    print('included_years = %s' % included_years, file=sys.stderr)

# Read included genres.
with open('genres.txt', 'r') as f:
    included_genres = f.read().split()
    # Print debug/info message to stderr
    print('included_genres = %s' % included_genres, file=sys.stderr)


# Process the input line by line.
for line in sys.stdin:

    # Parse the input line.
    uid, title, genres, year, rating = line.strip().split('\t')

    # Output the title and a count of 1.
    # Note: This IS NOT the CORRECT approach but should give you a useful starting point.
    print('%s\t%s' % (title, 1))
