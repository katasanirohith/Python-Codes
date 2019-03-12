def count_substring(s1, s2):
    # s1 = str(input())
    # s2 = str(input())
    ans = 0
    count = 0

    for i in range(0, len(s1)):
        if s1[i] == s2[0]:
            temp = 0
            count = 0
            for j in range(i, i + len(s2)):
                # print(s1[j], s2[temp])
                if i + len(s2) < len(s1) + 1:
                    if s1[j] == s2[temp]:
                        count += 1
                    if count == len(s2):
                        ans += 1
                temp += 1

    return ans


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)