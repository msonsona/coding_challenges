#!/bin/python3

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

    # First will sort the array
    arr.sort()
    
    # Then will sum all positions except the last for min
    min_sum = sum(arr[:-1])
    # And will sum all positions except the first for the max
    max_sum = sum(arr[1:])

    # Finally print as expected
    print(f"{min_sum} {max_sum}")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
