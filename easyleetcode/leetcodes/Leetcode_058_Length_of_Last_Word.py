class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        temp = s.split(' ')
        temp = [t for t in temp if len(t) > 0]
        if len(temp) == 0:
            return 0
        else:
            return len(temp[-1])

class Solution2:
    def strc(self, s):
        end = len(s) - 1
        # 取到最后一个字母所在位置的后一位
        while end > 0 and s[end] == ' ':
            end -= 1
        end = end + 1
        start = end - 1
        # 取到最后一个单词的首字母位置
        while start > 0 and s[start] != ' ':
            start -= 1
        start = start + 1
        L = end - start

        return L, s[start:end]


if __name__ == '__main__':
    strs=' hello word is good '
    s1 = Solution()
    print(s1.lengthOfLastWord(strs))
    s2 = Solution2()
    print(s2.strc(strs))
