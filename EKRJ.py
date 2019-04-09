n , m = input().split()
n = int(n)
m = int (m)
a = []
for i in range (0,n):
    a.append(0)
    for j in range(0, m):
        a.append([])
        a[i][j]=int(input())
