#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    max_distance = 0

    # If there is a single city, by definition, it will have a SS
    if n == 1:
        return max_distance

    # If there are as much SS as cities, distance will also be 0
    if n == len(c):
        return max_distance

    # If we aren't in the simple cases, then sort the array of SS
    c.sort()

    # Initialize from the distance of the 1st SS (at c[0]) to the 1st city (at 0)
    max_distance = c[0] - 0 
    i = 1
    while i < len(c):
        current_distance = (c[i] - c[i - 1]) // 2
        if current_distance > max_distance:
            max_distance = current_distance

        i += 1

    # Finally check with the distance between last SS (at c[-1]) and last city (at n - 1)
    last_distance = (n - 1) - c[-1]
    if last_distance > max_distance:
        max_distance = last_distance

    return max_distance

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
