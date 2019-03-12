# x , y = input().split()
#
# s = list(map(int,input().split()))
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# s = set(s)
# a = set(a)
# b = set(b)
# h = len(set.intersection(s,a))
# s = len(set.intersection(s,b))
# print(h-s)
# # count = 0
# # for a in s:
# #     count += 1
# # print(count)
x , y = input().split()
s = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
happy = 0
for i in s:
    if i in a:
        happy += 1
    elif i in b:
        happy -= 1
print(happy)