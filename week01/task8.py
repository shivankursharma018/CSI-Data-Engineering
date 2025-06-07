# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formated(num):
    if num < 1 or num > 99:
        print("constraint error")
    else:
        width = len(bin(num)) - 2

        for i in range(1, num+1):
            decimal = str(i)
            octal = oct(i)[2:]
            hexadecimal = hex(i)[2:].upper()
            binary = bin(i)[2:]
            print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}")

num = int(input())
print_formated(num)