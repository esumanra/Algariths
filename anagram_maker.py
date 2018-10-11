#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    need_removal_from_first_string = 0
    last_occ_ele_index = {}
    for ele in a:
        search_from_index = last_occ_ele_index.get(ele, 0)
        index = b[search_from_index:].find(ele)
        if index is not -1:
            last_occ_ele_index[ele] = index + search_from_index + 1
        else:
            need_removal_from_first_string += 1
    common_ele_count = len(a) - need_removal_from_first_string
    # total_removal_count = need_removal_from_first_string + len(b) - common_ele_count
    total_removal_count = len(a) + len(b) - 2 * common_ele_count

    print(last_occ_ele_index)
    return total_removal_count

a = "cdecc"

b = "abcc"

res = makeAnagram(a, b)

a = "fcrxzwscanmligyxyvym"
b = "jxwtrhvujlmrpdoqbisbwhmgpmeoke"

res = makeAnagram(a, b)
print(res)