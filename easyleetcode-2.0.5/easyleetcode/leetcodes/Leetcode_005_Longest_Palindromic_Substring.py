# 1穷举
class Solution:
    def str(self, s):
        if not s:
            return ''
        n = len(s)
        logest, left, right = 0, 0, 0
        for i in range(0, n):
            for j in range(i + 1, n + 1):
                substr = s[i:j]
                if self.isPalindrome(substr) and len(substr) > logest:
                    logest = len(substr)
                    left, right = i, j
        return s[left:right]

    def isPalindrome(self, s):
        if not s:
            return False
        return s == s[::-1]


class Solution2:
    def str(self, s):
        if s == None or len(s) == 0:
            return s
        res = ''
        for i in range(len(s)):
            # 奇数情况
            t = self.pali(s, i, i)
            if len(t) > len(res):
                res = t
            #     偶数情况
            t = self.pali(s, i, i + 1)
            if len(t) > len(res):
                res = t
        return res

    def pali(self, s, l, r):
        # 只要是回文串，就一直扩充
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # l+1 !!
        return s[l + 1:r]


if __name__ == '__main__':
    s = Solution()
    # s2 = Solution2()
    print(s.str('abcdzdcab'))
    # print(s2.str('abcdzdcab111'))
