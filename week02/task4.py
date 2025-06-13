def alphabet_rangoli(size):
    s = 'A'
    size = 5
    size += 2
    j = size-1
    k = size-1
    for i in range(1,size,2):
        print('-'*j+'-'.join(s*i)+'-'*k)
        j = j-2
        k = k-2
    j = 0
    k = 0
    for m in range(size,0,-2):
        print('-'*j+'-'.join(s*m)+'-'*k)
        j = j+2
        k = k+2

size = int(input())
alphabet_rangoli(size)
# 3
# 3 2 1 2 3
for i in range(size, 0, -1):
    initial_char = chr(97+i-1)
    print(initial_char, end='')
for j in range(2, size+1):
    later_char = chr(97+j-1)
    print(later_char, end='')
