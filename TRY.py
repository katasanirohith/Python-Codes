# liste = [x for x in range(0, 11)]
# print(liste)
x = int(input())
y = int(input())
z = int(input())
n = int (input())
listes = []
for i in range (0,x+1):
    for j in range (0,y+1):
        for k in range(0,z+1):
            if (i+j+k != n):
                listes.append([i,j,k])

print(listes)