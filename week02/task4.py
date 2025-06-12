def alphabet_rangoli(size):
    for i in range(0, size+1):
        # print('-', end='')

        for j in range(0, i):
            print('#', end='-')
    
        print(('-'*(size-i-1)), end='')
        print()
        print(('-'*(size-i-1)), end='')


    print('-', end='')
    for m in range(size-1, 0, -1):
        # print('-', end='')

        for n in range(0, m):
            print('#', end='-')

        print(('-'*(size-m-1)), end='')
        print()
        print(('-'*(size-m+1)), end='')

size = int(input())
alphabet_rangoli(size)