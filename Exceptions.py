n = int(input())

def fucn():
    a , b =input().split()
    try:
        print(int(a)/int(b))
    except ZeroDivisionError as e:
        print("Error Code: ",e)
    except ValueError as e:
        print("Error Code: ",e)
    except Inte




for i in range(0,n):
    fucn()