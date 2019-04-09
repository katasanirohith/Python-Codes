n = int(input())
unsorted =[]
for i in range(0,n):
    unsorted.append(int(input()))
a = []
for s in sorted(unsorted, key=int):
    print(s)
