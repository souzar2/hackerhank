#!/bin/python3

import os
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    j = 0
    k = 0
    
    cont = 0
    for i in a:
        if i > b[cont]:
            j += 1
        elif i < b[cont]:
            k += 1
        cont += 1
    res  = [j,k]
    return res


#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    #
    # Write your code here.
    #
    j=0
    for i in ar:
        j+=i
    return j

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
