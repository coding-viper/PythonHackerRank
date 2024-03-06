#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    i = int(input().strip())
    if i & 1 != 0:
        print("Weird")
    else:
        if i >= 2 and i <= 5:
            print("Not Weird")
        elif i >= 6 and i <= 20:
            print("Weird")
        elif i > 20 :
            print("Not Weird")
