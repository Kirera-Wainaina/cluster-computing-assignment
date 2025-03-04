#!/usr/bin/env python3

# Note: Don't change the next line.
from pyspark import SparkContext
from decimal import Decimal
import sys

# Student ID: 0000000

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
lines = sc.textFile('ratings.txt')

# Parse and explode genres, filter years/genres
def parse_line(line):
    try:
        uid, title, genres, year, rating = line.split('\t')
        rating = Decimal(rating)
        genres = genres.split('|')
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
    .map(lambda record: ((record[0], record[1]), (record[2], 1)))  # (genre, title), (rating, 1)
    .reduceByKey(lambda sum_and_count, sum_and_count2: (sum_and_count[0] + sum_and_count2[0], sum_and_count[1] + sum_and_count2[1])))  # Sum ratings and counts

# Filter by min_votes and compute averages
min_votes = 15
averages = (aggregated
    .filter(lambda key_agg: key_agg[1][1] >= min_votes)  # Keep if rating_count >= 15
    .map(lambda key_agg: (key_agg[0][0], (key_agg[0][1], key_agg[1][0] / key_agg[1][1])))  # (genre, (title, avg))
)

# Find max average per genre with ties
def find_max_per_genre(genre_group):
    genre = genre_group[0]
    title_avg_pairs = list(genre_group[1])  # List of (title, avg)
    if not title_avg_pairs:
        return []
    max_avg = max(pair[1] for pair in title_avg_pairs)
    max_titles = [pair[0] for pair in title_avg_pairs if pair[1] == max_avg]
    return [f"{genre}\t{title}\t{max_avg:.4f}" for title in max_titles]

results = (averages
    .groupByKey()  # Group by genre
    .flatMap(find_max_per_genre)  # Find max-rated movies per genre
    .collect())

# Note: Don't change the next line.
print('\n'.join(results), file=open('results.txt', 'w'))

# Note: Don't change the next line.
sc.stop()
