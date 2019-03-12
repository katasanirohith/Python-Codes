import textwrap


def wrap(string, max_width):
    teste = textwrap.fill(string, max_width)
    print(teste)
    return teste


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)