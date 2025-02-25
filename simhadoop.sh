#!/usr/bin/env bash

cat coffee.txt | ./mapper.py | sort | ./combiner.py | sort | ./reducer.py > results.txt