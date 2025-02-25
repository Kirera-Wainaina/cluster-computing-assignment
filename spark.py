#!/usr/bin/env python3
 
# Note: Don't change the next line.
from pyspark import SparkContext


# Student ID: 0000000


# Note: Don't change the next line.
sc = SparkContext('local', 'myapp')


# Note: The code in this next statement does not solve the problem that
# you have been given but it does give you the starting point of 
# a Spark RDD. You will need to make significant additions to this code to
# implement a solution that yields the correct results.
results = (sc
           .textFile('r5.txt')
           .collect())


# Note: Don't change the next line.
print('\n'.join(results), file=open('results.txt', 'w'))

# Note: Don't change the next line.
sc.stop()
