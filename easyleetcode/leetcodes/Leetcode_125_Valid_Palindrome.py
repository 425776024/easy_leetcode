class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alnum_s = [t.lower() for t in s if t.isalnum()]
        ls = len(alnum_s)
        if ls <= 1:
            return True
        mid = ls / 2
        for i in range(mid):
            if alnum_s[i] != alnum_s[ls - 1 - i]:
                return False
        return True

class Solution2:

    def isPalindrome(self, s):
        if not s:
            return True

        l, r = 0, len(s) - 1

        while l < r:
            # 是否是字母和数字，不是的忽略
            # isalnum! isalnum!
            while not s[l].isalnum():
                l += 1
            while not s[r].isalnum():
                r -= 1
            # 相同则+1，-1
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True

print('<iframe src="//player.bilibili.com/player.html?aid=626179101&bvid=BV1zt4y197rm&cid=208408787&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')
if __name__ == '__main__':
    s1 = Solution2()
    print(s1.isPalindrome('    A 2man, a plan, a can  al:   Panam2a   '))
    s2 = Solution2()
    print(s2.isPalindrome('    A 2man, a plan, a can  al:   Panam2a   '))
