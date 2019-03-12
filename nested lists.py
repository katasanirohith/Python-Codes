n = int (input())
list = []
lis2 = []
for i in range (n):
    name = input()
    score = int(input())
    list.append([score,name])
    lis2.append(score)
lis2.sort()
max = lis2[n-1]
bla=0
for i in lis2:
    if max == i:
        bla-=1
        seco=lis2[bla]
    bla+=1
result=[]
print(seco)
for i in range(0,n):

    if seco == list[i][0]:
        print("hey"+i)
        print(list[i][0])
        result.append(list)
print(result)
