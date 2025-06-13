# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=false

from collections import Counter

no_of_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
no_of_customers = int(input())

counter = dict(Counter(shoe_sizes))
print(counter)

sum = 0
for i in range(no_of_customers):
    bill = input().split()
    order_size = int(bill[0])
    price = int(bill[1])

    if order_size in counter:
        if counter[order_size] != 0:
            sum += price
            counter[order_size] -= 1
        else:
            continue

print(sum)
