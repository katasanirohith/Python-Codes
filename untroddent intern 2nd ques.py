a = list(map(int, input().split()))
a.sort()
n = len(a)
if n % 2 == 0:
    for i in range(0, int((n/2))):
            print(a[i], a[n-i-1], end=" ")
else:
    for i in range(0, int((n / 2)+1)):
        if i != int(n/2):
            print(a[i], a[n - i - 1], end=" ")
        else:
            print(a[int(n/2)])

