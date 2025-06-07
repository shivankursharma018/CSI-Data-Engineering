# using python 2
# https://www.hackerrank.com/challenges/python-tuples/problem

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = list(map(int, raw_input().split()))
    tup = tuple(integer_list)
    print(hash(tup))

