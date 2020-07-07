class Solution:
    def str(self, s):
        if len(s) == 0:
            return ''
        temp = []
        i = 0
        while i < len(s):
            j = i
            # isspace！！
            while j < len(s) and not s[j].isspace():
                j += 1
            if j != i:
                temp.append(s[i:j])
            # position j is space
            i = j + 1
        i = len(temp) - 1
        s = ''
        while i > 0:
            s += temp[i]
            s += ' '
            i -= 1
        s += temp[i]
        return s

print('<iframe src="//player.bilibili.com/player.html?aid=968657583&bvid=BV1rp4y1U7zY&cid=208408573&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')
if __name__ == '__main__':
    s = '     the     sky    is   blue'
    # 单词反转，如果多个空格，整理成正常形式
    # 借助isspace(),如果是空格则继续往下，直到遇到字母，截取单词
    sou = Solution()
    print(sou.str(s))
