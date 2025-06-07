# https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=false
def is_leap(year):
    if year < 1900 or year > 10**5:
        return "invalid year"
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
            else:
                leap = False
    return leap

year = int(input())
print(is_leap(year))