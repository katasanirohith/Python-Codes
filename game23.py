a , b = list(map(int,input().split()))
a = int(a)
b = int(b)
sum = b/a
count = 0
if b%a != 0:
    print(-1)
elif sum == 1:
    print(0)
else:
    while(1):
        if sum == 1:
            print(count)
            break
        elif sum % 6 == 0:
            sum = sum/6
            count += 2
        elif sum%2 ==0:
            sum = sum/2
            count =count+1
        elif sum % 3 == 0:
            sum = sum/3
            count +=1
        elif sum%2 ==0:
            sum = sum/2
            count =count+1



