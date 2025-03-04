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

# Read included years
with open('years.txt', 'r') as f:
    included_years = set(f.read().split())
    # print('included_years = %s' % included_years, file=sys.stderr)

# Read included genres
with open('genres.txt', 'r') as f:
    included_genres = set(f.read().split())
    # print('included_genres = %s' % included_genres, file=sys.stderr)

for line in sys.stdin:
    try:
        uid, title, genres, year, rating = line.strip().split('\t')
        genres = genres.split('|')

        if year not in included_years:
            continue

        for genre in genres:
            if genre in included_genres:
                # Output: key\t rating_sum \t rating_count (count is 1 for mapper)
                print(f"{title}|{genre}\t{rating}\t1")
    except Exception as e:
        print(f"Error in line: {line.strip()} - {str(e)}", file=sys.stderr)
