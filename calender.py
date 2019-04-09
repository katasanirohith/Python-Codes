import itertools
a = [1,2,3]
b = []
for i in range(1,len(a)+1):
    b.append(list(itertools.combinations(a,i)))
print(b[1][1]+b[1][2]