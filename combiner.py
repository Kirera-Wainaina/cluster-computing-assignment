#!/usr/bin/env python3

# Student ID: 3367315

import sys
from decimal import Decimal

current_genre = None
current_title = None
rating_sum = Decimal('0')
rating_count = 0

for line in sys.stdin:
    try:
        genre, title, rating_sum_str, rating_count_str = line.strip().split('\t')
        rating_sum_input = Decimal(rating_sum_str)
        rating_count_input = int(rating_count_str)

        key = (genre, title)
        if (current_genre, current_title) != key:
            if current_genre is not None:
                print(
                    f"{current_genre}\t{current_title}\t{rating_sum}\t{rating_count}")
            current_genre = genre
            current_title = title
            rating_sum = rating_sum_input
            rating_count = rating_count_input
        else:
            rating_sum += rating_sum_input
            rating_count += rating_count_input

    except Exception as e:
        print(f"Error in line: {line.strip()} - {str(e)}", file=sys.stderr)

if current_genre is not None:
    print(f"{current_genre}\t{current_title}\t{rating_sum}\t{rating_count}")
