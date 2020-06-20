def replaceBlank(str, length):
    s = ''
    for i in range(length):
        if str[i] == ' ':
            str[i] = '%20'
        s += str[i]
    return s


if __name__ == '__main__':
    str = "Mr John Smith"
    str = list(str)
    a = replaceBlank(str, len(str))
    print(a)
