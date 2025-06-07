# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formated(num):
    for i in range(1, num+1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]
        print(f"{decimal:>3} {octal:>3} {hexadecimal:>3} {binary:>3}")
num = int(input())
print_formated(num)