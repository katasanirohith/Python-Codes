import collections
import json
n =int (input())
o = collections.OrderedDict()
for i in range(0,n):
    stri = list(input().split())
    name =[]

    for i in stri:
        if i.isdigit():
            number=i
        else:
            name.append(i)
    temp=" ".join(name)

    if temp in o:
        o[temp] = int(o[temp]) + int(number)
    else:
        o[temp]=number
#print(o)
for i in o:
    print(i,o[i])