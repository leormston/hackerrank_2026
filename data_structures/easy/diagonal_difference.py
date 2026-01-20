#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    count_one = 0
    count_two = -1
    total_one = 0 
    total_two = 0
    for i in arr:
        total_one += i[count_one]
        total_two += i[count_two]
        count_one += 1
        count_two -=1 
    
    print(total_one)
    print(total_two)
    
    total = total_one - total_two
    
    if total < 0:
        return -total 
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
