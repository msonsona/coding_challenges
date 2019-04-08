#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    
    # Initialize the maximum sum value at a lowest point
    max_hourglass_sum = -100
    for i in range(4):
        for j in range(4):
            # Perform the hourglass sum for the current position
            hourglass_sum = 0
            hourglass_sum += arr[i][j]
            hourglass_sum += arr[i][j+1]
            hourglass_sum += arr[i][j+2]
            hourglass_sum += arr[i+1][j+1]
            hourglass_sum += arr[i+2][j]
            hourglass_sum += arr[i+2][j+1]
            hourglass_sum += arr[i+2][j+2]

            # Compare with max and update if needed
            max_hourglass_sum = max(max_hourglass_sum, hourglass_sum)
            
    return max_hourglass_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
