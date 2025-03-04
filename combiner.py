#!/usr/bin/env python3

import sys
from decimal import Decimal

# Student ID: 3367315

current_key = None
rating_sum = Decimal('0')
rating_count = 0

for line in sys.stdin:
    try:
        key, rating = line.strip().split('\t')
        rating = Decimal(rating)

        if current_key != key:
            if current_key is not None:
                print(f"{current_key}\t{rating_sum}\t{rating_count}")
            current_key = key
            rating_sum = rating
            rating_count = 1
        else:
            rating_sum += rating
            rating_count += 1

    except Exception as e:
        print(f"Error in line: {line.strip()} - {str(e)}", file=sys.stderr)

# Output final group
if current_key is not None:
    print(f"{current_key}\t{rating_sum}\t{rating_count}")
