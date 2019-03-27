n = int(input())
b = list(map(int, input().split()))
count =0
count1 =0
a = b
for i in range(0,len(b)):
    a.append(b[i])
for i in range(0,2*n):
    if a[i] == 1:
        count += 1
        if count >= count1:
         count1 = count
    else:
            count = 0


print(count1)

