n = int(input())
b = list(map(int,input().split()))
a = []
for i in range(0,n):
    a.append(i+1)
for i in range(0,len(b)):
    for k in a:
        for j in a:
            if i!=j:
                if j - k == i:
                    print(k,j)

