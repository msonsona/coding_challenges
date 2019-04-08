#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    num_pairs = 0
    color_stacks = {}
    for sock in ar:
        # If it's the first sock of this color, initialize to 0
        if not sock in color_stacks:
            color_stacks[sock] = 0
        # Add one sock to this color stack
        color_stacks[sock] += 1
        # If stack "size" is multiple of 2, then increase the pair counter
        if color_stacks[sock] % 2 == 0:
            num_pairs += 1

    return num_pairs 



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
