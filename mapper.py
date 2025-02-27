#!/usr/bin/env python3

import sys


# Student ID: 3367315


"""
The problem is to analyse a list of movie review ratings to find the film title(s) with the highest average rating for
each genre, for a specified set of years and genres.

This mapper does the following:
    1. Reads the included years and genres from files.
    2. Processes and parses the input line by line.
    3. Splits genres into a list resulting in multiple lines.
    4. Checks if the resultant row has year and genre included in the list given.
    5. Skips rows with year and genre not included.
    6. Outputs lines with single genres.
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
            print('%s\t%s\t%s\t%s' %
                  (title, genre, year, rating))
