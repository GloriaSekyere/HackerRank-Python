#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if len(s) > 1 and len(s) < 1000:
        words = s.split(" ")
        capitalized = []
        for item in words:
            if item.isalpha():
                capitalized.append(item.title())
            else:
                capitalized.append(item)
        s = " ".join(capitalized)
        return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
