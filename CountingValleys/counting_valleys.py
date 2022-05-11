import math
import os
import random
import re
import sys



def countingValleys(steps, path):
    
    count_valley = []
    up = 0
    down = 0
    result = 0
    flag = False
    for step in path:
        if step == "U":
            up += 1
        else:
            down += 1
        if (up - down) < 0:
            flag = True
        else:
            if flag:
                result += 1
                flag = False
    return result
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
