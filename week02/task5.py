# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=false

def merge_tools(s, k):
    partition_list = []
    i = 0
    k_tmp = k
    while i < len(s):
        partition_list.append(s[i:k_tmp])
        i += k
        k_tmp += k

    # print(partition_list)
    for i in range(len(partition_list)):
        print(''.join(set(partition_list[i])))

s, k = input(), int(input())
merge_tools(s, k)