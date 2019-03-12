n = int(input())
a = list(map(int,input().split()))
maxi = max(a)
count = 1
maxa=0
a.sort()
for i in range (0,n):
    if(a[n-i-1]>= maxi-5 ):
        count += 1
        if count > maxa:
            maxa = count
    else:

        maxi = a[n-i-1]
        count = 1

print(maxa-1)