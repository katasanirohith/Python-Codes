n , b = input().split()
n = int(n)
sum1 = n
b = int(b)
a = list(map(int,input().split()))
count = 0
if sum(a) == 0:
    print(-1)
else:
    while sum1 > 0:
            k=0
            sum1 = sum1 + int(a[k])
            count += 1
            if k == n-1:
                k=0
            if sum1 <=0:
                break
print(count-1)




