#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def hash_values():
    height = 1
    count = 0
    period_type = "double"
    heights = []
    while count != 60:
        if period_type == "single":
            height += 1
            period_type = "double"
        else:
            height = height * 2
            period_type = "single"
        heights.append(height)
        count += 1
    return heights
def utopianTree(n):
    heights = hash_values()
    if n == 0:
        return 1
    return heights[n-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
