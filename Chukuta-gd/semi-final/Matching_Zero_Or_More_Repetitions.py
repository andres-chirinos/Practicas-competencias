#https://www.hackerrank.com/contests/chukuta-gd-semi-final/challenges/matching-zero-or-more-repetitions
Regex_Pattern = r'^\d{2,}([a-z]*)([A-Z]*)$'    # Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())