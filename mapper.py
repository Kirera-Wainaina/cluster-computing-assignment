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

    # Split genres into a list
    genres = genres.split('|')

    # check if year is included
    # skip if year is not included
    if year not in included_years:
        continue

    # Output lines with single genres
    for genre in genres:
        # skip if genre is not included
        if genre not in included_genres:
            continue
        else:
            print('%s\t%s\t%s\t%s\t%s' % (uid, title, genre, year, rating))
