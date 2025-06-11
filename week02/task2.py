# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=false
def avg(n, arr):
    height_set = set(arr)
    if n > 0 and n <= 100:
        sum = 0
        for i in height_set:
            sum += i
        avg = sum / len(height_set)
    return float(avg)

n = int(input())
arr = list(map(int, input().split()))
result = avg(n, arr)
print(result)
