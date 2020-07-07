
def isMatch2( s, p):
    s = '0' + s
    p = '0' + p
    # dp[i][j]表示：s的前i个字符与p的前j个字符是否匹配
    dp = [[False for _ in range(len(p))] for _ in range(len(s))]

    # 初始化
    dp[0][0] = True  # 空字符串与空字符串相匹配
    for i in range(1, len(p)):
        if p[i] == '*':
            # 取决于前面是否匹配
            dp[0][i] = dp[0][i - 1]

    # 动态规划
    for i in range(1, len(s)):
        for j in range(1, len(p)):
            if s[i] == p[j] or p[j] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    return dp[-1][-1]


def isMatch(s, p):
    i = 0
    j = 0
    # s串中0:iStart部分的字符串（在jStar位置星号的万能匹配下）与p中0:jStar部分完全匹配
    iStar = -1
    jStar = -1
    m = len(s)
    n = len(p)
    while i < m:
        # 好说，正常过
        if j < n and (s[i] == p[j] or p[j] == '?'):
            j += 1
            i += 1
        elif j < n and p[j] == '*':
            # *出现位置用jStar记住
            jStar = j
            # s串中0:iStart部分的字符串（在jStar位置星号的万能匹配下）与p中0:jStar部分完全匹配
            iStar = i
            # i不+1，因为*号也可以选择不匹配，也就是，遇到*号，你可以忽略。（axaaxabcdbc, ax*bc 。拿出第i=2,j=2,位置进行比较，s[i]=a,p[j]=*,
            # a和*不一样，*虽然可以万能匹配，让你i继续过，但是也可以不匹配，让*的后一个老哥p[j+1]=‘b’ 来和你匹配）
			# 反正，当*后面那个老哥不能出面消你的时候，*可以再出面做万能消除！所以不用+1
            j += 1
        elif iStar >= 0:
            # s中继续往后走，因为*万能匹中s中字符，需要这一步*来出面消除，则意味着把s中iStar前面的全部用p中jStar位的*来消除
            iStar += 1
            i = iStar
            # 如果到了需要*来万能解决出面的时候，j从新回到前面的*后一位
            j = jStar + 1
        else:
            # 这里，意味着？没有'*'，不想等或每个'？'取匹中s中的i位字符
            return False

    while j < n and p[j] == '*':
        j += 1
    return j == n

print('<iframe src="//player.bilibili.com/player.html?aid=371200662&bvid=BV1dZ4y1M7BX&cid=208409531&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')

'''
虽然*能匹配任意串，但是p中*后面出现字符不在s中，就断了
'''

print(isMatch("axaaxabcdbc", "ax*bc"))
print(isMatch("aa", "a*"))
print(isMatch("ab", "?*"))
