x = input()
y = input()
ans = 0
for i in x:
    count = 1
    for j in y:
        if i != j:
            break
        else:
            count += 1
            i+=1
    if count == len(y):
        ans += 1
print(ans)