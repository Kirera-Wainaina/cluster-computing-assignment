#!/usr/bin/env python3

# Note: Don't change the next line.
from pyspark import SparkContext
from decimal import Decimal
import sys

# Student ID: 3367315

# Note: Don't change the next line.
sc = SparkContext('local', 'myapp')

# Read filter files
with open('years.txt', 'r') as f:
    included_years = set(f.read().split())
    print(f"included_years = {included_years}", file=sys.stderr)

with open('genres.txt', 'r') as f:
    included_genres = set(f.read().split())
    print(f"included_genres = {included_genres}", file=sys.stderr)

# Load ratings data
lines = sc.textFile('r5.txt')

# Parse and explode genres, filter years/genres


def parse_line(line):
    try:
        uid, title, genres, year, rating = line.split('\t')
        rating = Decimal(rating)
        genres = genres.split('|')
        # Yield (genre, title, rating) tuples, applying filters
        for genre in genres:
            if (not included_years or year in included_years) and \
               (not included_genres or genre in included_genres):
                yield (genre, title, rating)
    except Exception as e:
        print(f"Error parsing line: {line} - {str(e)}", file=sys.stderr)


ratings = lines.flatMap(parse_line)

# Aggregate ratings by (genre, title)
# Map to ((genre, title), (rating_sum, rating_count))
aggregated = (ratings
              # (genre, title), (rating, 1)
              .map(lambda x: ((x[0], x[1]), (x[2], 1)))
              .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])))  # Sum ratings and counts

# Filter by min_votes and compute averages
min_votes = 15
averages = (aggregated
            # Keep only if rating_count >= 15
            .filter(lambda x: x[1][1] >= min_votes)
            # (genre, (title, avg))
            .map(lambda x: (x[0][0], (x[0][1], x[1][0] / x[1][1])))
            )

# Find max average per genre with ties


def find_max_per_genre(records):
    genre = records[0]
    movies = list(records[1])  # List of (title, avg)
    if not movies:
        return []
    max_avg = max(movie[1] for movie in movies)
    max_titles = [movie[0] for movie in movies if movie[1] == max_avg]
    return [f"{genre}\t{title}\t{max_avg:.4f}" for title in max_titles]


results = (averages
           .groupByKey()  # Group by genre
           .flatMap(find_max_per_genre)  # Find max-rated movies per genre
           .collect())

# Note: Don't change the next line.
print('\n'.join(results), file=open('results.txt', 'w'))

# Note: Don't change the next line.
sc.stop()
