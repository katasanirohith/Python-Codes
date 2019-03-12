s = str(input())
s = list(s)
a=0
for i in s:
    if i.isupper():
        s[a]=i.lower()
    else:
        s[a]=i.upper()
    a+=1
s="".join(s)
print(s)