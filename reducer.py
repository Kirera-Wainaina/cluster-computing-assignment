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

current_genre = None
genre_movies = {}  # {title: (rating_sum, rating_count)}
min_votes = 15

for line in sys.stdin:
    try:
        key, rating_sum_str, rating_count_str = line.strip().split('\t')
        genre, title = key.split('|')
        rating_sum_input = Decimal(rating_sum_str)
        rating_count_input = int(rating_count_str)

        # If genre changes, process the previous genre
        if current_genre != genre and current_genre is not None:
            # Calculate averages and find max
            max_avg = Decimal('-infinity')
            movies_by_avg = {}  # {avg: [list of titles]}

            for title, (rating_sum, rating_count) in genre_movies.items():
                if rating_count >= min_votes:
                    avg = rating_sum / rating_count
                    if avg not in movies_by_avg:
                        movies_by_avg[avg] = []
                    movies_by_avg[avg].append(title)
                    max_avg = max(max_avg, avg)

            # Output all movies with the max average
            if max_avg != Decimal('-infinity'):
                for title in movies_by_avg.get(max_avg, []):
                    print(f"{current_genre}\t{title}\t{max_avg}")

            # Reset for new genre
            genre_movies = {}

        # Update current genre and accumulate data
        current_genre = genre
        if title in genre_movies:
            prev_sum, prev_count = genre_movies[title]
            genre_movies[title] = (
                prev_sum + rating_sum_input, prev_count + rating_count_input)
        else:
            genre_movies[title] = (rating_sum_input, rating_count_input)

    except Exception as e:
        print(f"Error in line: {line.strip()} - {str(e)}", file=sys.stderr)

# Process the final genre
if current_genre is not None:
    max_avg = Decimal('-infinity')
    movies_by_avg = {}

    for title, (rating_sum, rating_count) in genre_movies.items():
        if rating_count >= min_votes:
            avg = rating_sum / rating_count
            if avg not in movies_by_avg:
                movies_by_avg[avg] = []
            movies_by_avg[avg].append(title)
            max_avg = max(max_avg, avg)

    if max_avg != Decimal('-infinity'):
        for title in movies_by_avg.get(max_avg, []):
            print(f"{current_genre}\t{title}\t{max_avg}")
