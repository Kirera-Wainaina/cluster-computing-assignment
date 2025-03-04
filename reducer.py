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

current_key = None
total_sum = Decimal('0')
total_count = 0
min_votes = 15

for line in sys.stdin:
    try:
        # Split input: key (title|genre) and sum/count from combiner
        fields = line.strip().split('\t')
        if len(fields) != 3:
            print(f"Invalid line: {line.strip()}", file=sys.stderr)
            continue

        key, rating_sum, rating_count = fields
        rating_sum = Decimal(rating_sum)
        rating_count = int(rating_count)

        if current_key != key:
            if current_key is not None and total_count >= min_votes:
                avg_rating = total_sum / total_count
                title, genre = current_key.split('|')
                print(f"{title}\t{genre}\t{avg_rating}")

            current_key = key
            total_sum = rating_sum
            total_count = rating_count
        else:
            total_sum += rating_sum
            total_count += rating_count

    except Exception as e:
        print(f"Error in line: {line.strip()} - {str(e)}", file=sys.stderr)

# Output final group
if current_key is not None and total_count >= min_votes:
    avg_rating = total_sum / total_count
    title, genre = current_key.split('|')
    print(f"{title}\t{genre}\t{avg_rating}")
