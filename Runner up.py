n = int(input())
narr = input().split()
narr = [int(x) for x in narr]
narr.sort()
max = narr[n-1]
bla=0
for x in narr:
    if(x == max):
        bla -= 1
        print(narr[bla])
        break
    bla+=1

