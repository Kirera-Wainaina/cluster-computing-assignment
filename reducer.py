#!/usr/bin/env python3

import sys
from decimal import Decimal


# Student ID: 3367315


#  *** Note: This should be set to 15 in your submitted code.
#
# You will want to set it to 15 when running against the large ratings.txt data file.
# You will want to set it to 1 or 2 when running against the smaller r5.txt and r100.txt files
# otherwise films with small numbers of votes will be prevented from producing results.
min_votes = 15
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

def process_genre(genre, movies, min_votes):
    max_avg = Decimal('-infinity')
    max_titles = []

    for title, (rating_sum, rating_count) in movies.items():
        if rating_count >= min_votes:
            avg = rating_sum / rating_count
            if avg > max_avg:
                max_avg = avg
                max_titles = [title]
            elif avg == max_avg:
                max_titles.append(title)

    if max_avg != Decimal('-infinity'):
        for title in max_titles:
            print(f"{genre}\t{title}\t{max_avg:.4f}")


current_genre = None
genre_movies = {}
min_votes = 15

for line in sys.stdin:
    try:
        genre, title, rating_sum_str, rating_count_str = line.strip().split('\t')
        rating_sum_input = Decimal(rating_sum_str)
        rating_count_input = int(rating_count_str)

        if current_genre != genre and current_genre is not None:
            process_genre(current_genre, genre_movies, min_votes)
            genre_movies = {}

        current_genre = genre
        if title in genre_movies:
            prev_sum, prev_count = genre_movies[title]
            genre_movies[title] = (
                prev_sum + rating_sum_input, prev_count + rating_count_input)
        else:
            genre_movies[title] = (rating_sum_input, rating_count_input)

    except Exception as e:
        print(f"Error in line: {line.strip()} - {str(e)}", file=sys.stderr)

if current_genre is not None:
    process_genre(current_genre, genre_movies, min_votes)
