if __name__ == '__main__':
    s = input()
    result1=0
    result2=0
    result3=0
    result4=0
    result5=0
    for i in s:
        if i.isalnum():
            result1=1
        if i.isalpha():
            result2=1
        if i.isdigit():
            result3=1
        if i.islower():
            result4=1
        if i.isupper():
            result5=1
    if result1 == 0:
        print("False")
    else:
        print("True")
    if result2==0:
        print("False")
    else:
        print("True")
    if result3==0:
        print("False")
    else:
        print("True")
    if result4==0:
        print("False")
    else:
        print("True")
    if result5==0:
        print("False")
    else:
        print("True")




