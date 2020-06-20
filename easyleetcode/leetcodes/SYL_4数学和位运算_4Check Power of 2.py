

class Solution:
    def checkPowerOf2(self, n):
        if n < 1:
            return False
        else:
            # 偶数的时候为0
            c = n & (n - 1)
            return c == 0


s = Solution()
print(s.checkPowerOf2(16))
