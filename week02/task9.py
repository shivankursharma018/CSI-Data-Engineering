# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

set_len = int(input())
s = list(map(int, input().split()))

li = []
while set_len == len(s) and 0<set_len<20:    
    for i in range(set_len):
        li.append(s[i])

    s = set(li)

    no_cmds = int(input())

    for i in range(no_cmds):
        cmd = input().split()
        if 'pop' in cmd[0]:
            s.pop()
        elif 'remove' in cmd[0]:
            try:
                s.remove(int(cmd[1]))
            except KeyError:
                continue
        elif 'discard' in cmd[0]:
            try:
                s.discard(int(cmd[1]))
            except KeyError:
                continue

    sum = 0
    for j in range(len(s)):
        li2 = list(s)
        sum += li2[j]
    print(sum)