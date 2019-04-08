#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    # s is the string to repeat
    # n is the number of chars to scope the search for 'a'

    # Initialize the counter
    num_a = 0

    # Count the number of appearances of 'a' in s
    num_a_in_s = len([l in l for l in s if l == 'a'])

    # Compute the number of repetitions of the input string,
    # based on the amount of chars to consider
    repetitions, remainder_length = divmod(n, len(s))

    num_a = num_a_in_s * repetitions

    if remainder_length > 0:
        # If there are chars left, count the number of 'a' in the 
        # remainding substring
        remainding_a = len([l in l for l in s[:remainder_length] if l == 'a'])
        num_a += remainding_a

    return num_a 

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
