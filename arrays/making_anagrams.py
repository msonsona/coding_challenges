#!/bin/python3

import math
import os
import random
import re
import sys

def _countFreqs(s):
    freqs = {}

    for c in s:
        if not c in freqs:
            freqs[c] = 0
        freqs[c] += 1
    
    return freqs

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    freqs_a = _countFreqs(a)
    freqs_b = _countFreqs(b)

    keys_a = set(freqs_a.keys())
    keys_b = set(freqs_b.keys())

    chars_to_delete = 0

    for k in keys_a.intersection(keys_b):
        chars_to_delete += abs(freqs_a[k] - freqs_b[k])

    for k in keys_a.difference(keys_b):
        chars_to_delete += freqs_a[k]

    for k in keys_b.difference(keys_a):
        chars_to_delete += freqs_b[k]

    return chars_to_delete

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
