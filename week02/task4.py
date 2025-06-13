def alphabet_rangoli(size):
    total_width = 4 * size - 3

    # top half
    j = size - 1
    i = 1
    while i <= size:
        left = []
        ch = size
        count = 1
        while count < i:
            left.append(chr(96 + ch))
            ch -= 1
            count += 1

        right = []
        ch = size - i + 1
        while ch <= size:
            right.append(chr(96 + ch))
            ch += 1

        row = left + right
        print('-'.join(row).center(total_width, '-'))

        i += 1

    # bottom half
    i = size - 1
    while i >= 1:
        left = []
        ch = size
        count = 1
        while count < i:
            left.append(chr(96 + ch))
            ch -= 1
            count += 1

        right = []
        ch = size - i + 1
        while ch <= size:
            right.append(chr(96 + ch))
            ch += 1

        row = left + right
        print('-'.join(row).center(total_width, '-'))

        i -= 1

size = int(input())
alphabet_rangoli(size)