def LCstring(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1 + 1)] for j in range(len2 + 1)]
    result = 0
    # i or j =0时，res[i][j] =0
    # string1[i] = string2[j] 时，res[i][j] = res[i - 1][j - 1] + 1
    # string1[i] != string2[j] 时，res[i][j] = 0

    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if string2[i - 1] == string1[j - 1]:
                # 以string1[i-1], string2[j-1]为结尾的最长公共子串，长度是 res[i][j]
                res[i][j] = res[i - 1][j - 1] + 1
                result = max(result, res[i][j])
    return result

print('<iframe src="//player.bilibili.com/player.html?aid=968702301&bvid=BV1Rp4y1U7fj&cid=208094819&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')
print(LCstring("helloworld", "loop"))
# 输出结果为：2
