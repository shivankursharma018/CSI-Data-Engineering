# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=false

name = input()
def capitalize_name(name):
    li = name.split(' ')
    newlist=[]
    
    for i in range(0, len(li)):
        name = li[i].capitalize()
        newlist.append(name)
    
    name = ' '.join(newlist)
    return name

print(capitalize_name(name))