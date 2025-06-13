# https://www.hackerrank.com/challenges/exceptions/problem

t = int(input())
for i in range(t):
    try:
        a, b = list(map(int, input().split()))
        try:
            print(a//b)
        except ZeroDivisionError as ze:
            print(f"Error Code: integer division or modulo by zero")
    except ValueError as ve:
        print(f"Error Code: {ve}")
