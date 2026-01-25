#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    arr = sorted(arr)
    unique = set()
    for i in arr:
        unique.add(i)
    highest_count = arr.count(arr[0])
    highest_id = arr[0]
    for i in unique:
        occ = arr.count(i)
        if occ > highest_count:
            highest_count = occ
            highest_id = i
    return highest_id
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
