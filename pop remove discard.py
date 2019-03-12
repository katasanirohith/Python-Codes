n = int(input())
a = set(map(str, input().split()))
x = int(input())
for i in range(0,x):
    s = list(map(str,input().split()))
    if s[0] == 'pop':
        a.pop()
    if s[0] == 'remove':
        #print(s[1])
        if s[1] in a:
            a.remove(s[1])
    if s[0] == 'discard':
        a.discard(s[1])
    #print(a)

print(len(a))