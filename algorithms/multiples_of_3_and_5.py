#!/bin/python3

if __name__ == '__main__':
    # Print the sum of integers below 1000 that are multiple of 3 or 5
    print(sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]))

