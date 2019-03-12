import itertools

A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = list(itertools.product(A, B))
for i in s:
    print(i,end="")
