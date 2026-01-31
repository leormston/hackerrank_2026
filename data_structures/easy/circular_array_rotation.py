#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    length = len(a)
    shift_required =  k % length
    print(f"a: {a}")
    print(f"shift_required: {shift_required}")
    # new_array = a[shift_required:]
    new_array = []
    for index in range(len(a)-1, (len(a)-1) -shift_required , -1):
        print(f"index: {index}")
        new_array.insert(0, a[index])
    print(new_array)
    for index in range(0, (len(a) ) -shift_required, 1):
        print(f"index: {index}")
        new_array.append(a[index])
    print(new_array)
    results = []
    
    for q in queries:
        results.append(new_array[q])
    return results
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
