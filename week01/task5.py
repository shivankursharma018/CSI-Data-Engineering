# https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=false

from itertools import combinations

N = int(input())
input_str = input().split()
# print(input_str)

id = int(input())
select = 'a'

combs = list(combinations(input_str, id))
# print(combs)

fav_combs = 0
for c in combs:
    if select in c:
        fav_combs += 1
if len(combs) > 0:
    probability = fav_combs / len(combs)
    print(f"{probability}")
else:
    print("0")