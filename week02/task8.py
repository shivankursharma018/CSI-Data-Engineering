# https://www.hackerrank.com/challenges/incorrect-regex/problem
import re
t = int(input())
for i in range(t):
    regex_in = input()
    if re.compile(regex_in):
        print(True)
    else:
        print(False)