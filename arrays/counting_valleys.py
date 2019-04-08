#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    current_level = 0
    num_valleys = 0

    for step in s:
        if step == 'U':
            current_level += 1
        elif step == 'D':
            if current_level == 0:
                num_valleys += 1
            current_level -= 1

    return num_valleys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
