def print_formatted(number):
    for i in range(1, number+1):
        print(str(i).rjust(),oct(i)[2:], hex(i)[2:].upper() , bin(i)[2:])





if __name__ == '__main__':
    n = int(input())
    print_formatted(n)