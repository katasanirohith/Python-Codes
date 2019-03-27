n, k = input().split()
n = int(n)
k = int(k)
x1, y1 = input().split()
x1 = int(x1)
y1 = int(y1)
lis1 =[]
sum = 0
lis = []
for i in range (0,int(n)):
    lis.append([])
    for j in range(0,int(n)):
        lis[i].append(0)
        lis[i][j] = 0
lis[n-x1][y1-1] = 2
for i in range(0, int(k)):
    lis1.append(list(map(int, input().split())))
    a1 = int(n) - lis1[i][0]
    lis[a1][lis1[i][1]-1] = 1
x1 = n - x1
y1 = y1 - 1
count = 0
for i in range(y1+1, n):
    if lis[x1][i] == 0:
        count += 1
    else:
        break
for i in range(y1-1, -1, -1):
    if lis[x1][i] == 0:
        count += 1
    else:
        break
for i in range(x1+1, n):
    if lis[i][y1] == 0:
        count += 1
    else:
        break
for i in range(x1-1, -1, -1):
    if lis[i][y1] == 0:
        count += 1
    else:
        break
bu1 = x1 - 1
bu2 = y1 + 1
for i in range(x1+1, -1, -1):
    if bu1 >= 0 and bu2 < n:
        if lis[bu1][bu2] == 0:
            count += 1
            bu1 -= 1
            bu2 += 1
        else:
            break
bu1 = x1 + 1
bu2 = y1 + 1
for i in range(x1+1, n):
    if bu1 < n and bu2 < n:
        if lis[bu1][bu2] == 0:
            count += 1
            bu1 += 1
            bu2 += 1
        else:
            break
bu1 = x1 - 1
bu2 = y1 - 1
for i in range(x1-1, 0, -1):
    if bu1 >= 0 and bu2 >= 0:
        if lis[bu1][bu2] == 0:
            count += 1
            bu1 -= 1
            bu2 -= 1
        else:
            break
bu1 = x1 + 1
bu2 = y1 - 1
for i in range(x1+1, n):
    if bu1 < n and bu2 >= 0:
        if lis[bu1][bu2] == 0:
            count += 1
            bu1 += 1
            bu2 -= 1
        else:
            break
print(count)