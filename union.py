x = int(input())
a = set(map(int,input().split()))
y = int(input())
b = set(map(int,input().split()))
print(len(a.union(b)))