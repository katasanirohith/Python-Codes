s = input()
count = 0
s1 = ['h','e','l','l','o']
i = 0
j = 0
while(i<len(s) and j <len(s1)):
    if(s[i] == s1[j]):
        count+=1
        i+=1
        j+=1
    else:
        i+=1
if count == 5:
    print("YES")
else:
    print("NO")



