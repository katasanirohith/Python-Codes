s = str(input())
s = list(s)
a = 0
s1 = 'r'
s[0]
print(s1)
for i in s:
    print(i)
    if i == " ":
        s[a+1] = s[a+1].upper()
    a += 1
print(s)
