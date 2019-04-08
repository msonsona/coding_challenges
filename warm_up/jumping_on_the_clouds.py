#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    index = 0
    clouds_length = len(c)
    num_jumps = 0

    print(f"Seq. length = {clouds_length}")

    # Advance through the clouds
    while index < clouds_length - 1:
        print(f"Index = {index}")
        # First try to jump two (if possible)
        next_index = index + 2
        if next_index < clouds_length and c[next_index] == 0:
            print(f"Jumping 2")
        # If not, jump one
        else:
            print(f"Jumping 1")
            next_index = index + 1

        # Update the index
        index = next_index
        print(f"After jumping, index is {index}")
        # Count the additional jump
        num_jumps += 1
        print(f"Number of jumps so far = {num_jumps}")

    return num_jumps


def test(test_clouds):
    clouds = list(map(int, test_clouds.split()))
    print(jumpingOnClouds(clouds))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()


