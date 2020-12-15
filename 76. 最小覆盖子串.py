# s= "AOAEEGCBCBCBCA"  t= "ABC"
from collections import defaultdict

def minWindow(s: str, t: str):
    ture_dict = defaultdict(int)
    for c in t:
        ture_dict[c] == 1
    compare_dict = defaultdict(int)
    right = left = 0

    for c in s:
        if c in ture_dict:
