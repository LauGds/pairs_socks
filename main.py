import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    set_ar = set(ar)
    pairs = 0
    for i in set_ar:
        pairs += ar.count(i) // 2
    return pairs
