
def isMatch(s, p):
    i = 0
    j = 0
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
            # *出现位置j
            jStar = j
            # 星号匹配到s串中的位置
            iStar = i
            j += 1
        # 前面，出现过*，不好说，特殊处理
        elif iStar >= 0:
            # s中继续往后走，因为*万能匹中s中字符
            iStar += 1
            i = iStar
            # 如果到了需要*来万能解决出面的时候
            # p中继续往后无论多远的j，都要回来，（jStar永远记录着*号出现位置，直到下一个*出现），回到jStar 下一个位置
            # "xxxxxa b c d  bce", "*bce ： 前面一波操作，xxxxxa vs *  匹中（ i=5  jStar=0 j = 1 p[j]=b）
            # "xxxxxa b c d  bce", "*bce ： b vs b  匹中 （i=6 j=1 >进第一个if进行++）
            # "xxxxxa b c d  bce", "*bce ： c vs c  匹中 （i=7 j=2 >进第一个if进行++）
            # "xxxxxa b c d  bce", "*bce ： c vs c  匹中 （i=7 j=2 >进第一个if进行++）
            # "xxxxxa b c d  bce", "*bce ： d vs e  不匹中 （i=8 j=8 >进万能 * elif iStar >= 0，j回到*位置后面，i前面的被*全部管住，重新开始匹配）
            # "xxxxxa b c d  bce", "*bce ： b vs b  匹中 （i=9 j=1）
            # "xxxxxa b c d  bce", "*bce ： c vs c  匹中 （i=10 j=2）
            # "xxxxxa b c d  bce", "*bce ： e vs e  匹中 （i=11 j=3）
            j = jStar + 1
        else:
            # 这里，意味着？没有'*'，不想等或每个'？'取匹中s中的i位字符
            return False

    while j < n and p[j] == '*':
        j += 1
    return j == n


'''
虽然*能匹配任意串，但是p中*后面出现字符不在s中，就断了
'''

# print(isMatch("aa", "a"))
# print(isMatch("aaa", "aa"))
print(isMatch("xxxxxabcdbc", "*bc"))
print(isMatch("aa", "a*"))
print(isMatch("ab", "?*"))
