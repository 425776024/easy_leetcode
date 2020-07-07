def printflsc(x, y):
    global flag, string1, string2, s
    # 回溯输出最长公共子序列
    if x == 0 or y == 0:
        return None
    if flag[x][y] == 1:
        # 意味着曾经触发：string2[i - 1] == string1[j - 1]
        printflsc(x - 1, y - 1)
        # 数组是0开始，所以x-1
        s += string2[x - 1]
    elif flag[x][y] == 2:
        # 意味着曾经触发：res[i - 1][j] >= res[i][j - 1]，
        printflsc(x - 1, y)
    else:
        # # 意味着曾经触发：res[i - 1][j] < res[i][j - 1]
        printflsc(x, y - 1)


def LCS(string1, string2):
    res = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]

    #  截止到以string1[i-1], string2[j-1]！！ 的最长公共子序列长度是 res[i][j]
    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if string2[i - 1] == string1[j - 1]:
                res[i][j] = res[i - 1][j - 1] + 1
                flag[i][j] = 1
            else:
                # 不相等，并不影响序列！顶多就是此轮序列长度不+1，那还可以为上一轮序列长度啊
                res[i][j] = max(res[i - 1][j], res[i][j - 1])
                if (res[i - 1][j] >= res[i][j - 1]):
                    flag[i][j] = 2
                else:
                    flag[i][j] = 3
    return res, res[-1][-1]

print('<iframe src="//player.bilibili.com/player.html?aid=201134913&bvid=BV12z411e7vg&cid=208094617&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')
if __name__ == '__main__':
    string1 = 'helloworld'
    string2 = 'loop'
    len1 = len(string1)
    len2 = len(string2)
    flag = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]

    s = ''
    r, l = LCS(string1, string2)
    print(l)
    printflsc(len2, len1)
    print(s)
