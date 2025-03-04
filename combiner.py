#!/usr/bin/env python3

import sys
from decimal import Decimal

# Student ID: 3367315

current_key = None
rating_sum = Decimal('0')
rating_count = 0

for line in sys.stdin:
    try:
        key, rating_sum_str, rating_count_str = line.strip().split('\t')
        rating_sum_input = Decimal(rating_sum_str)
        rating_count_input = int(rating_count_str)

        if current_key != key:
            if current_key is not None:
                print(f"{current_key}\t{rating_sum}\t{rating_count}")
            current_key = key
            rating_sum = rating_sum_input
            rating_count = rating_count_input
        else:
            rating_sum += rating_sum_input
            rating_count += rating_count_input

    except Exception as e:
        print(f"Error in line: {line.strip()} - {str(e)}", file=sys.stderr)

if current_key is not None:
    print(f"{current_key}\t{rating_sum}\t{rating_count}")
