# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
from itertools import groupby
s = input()
keys = []
group = []

for k in groupby(s):
    keys.append(k[0])
    group.append(k[1])
for k, g in groupby(s):
    print(f"({len(list(g))}, {k})", end=' ')
