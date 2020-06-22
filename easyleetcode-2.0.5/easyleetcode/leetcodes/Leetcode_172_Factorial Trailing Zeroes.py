

class Solution:
    def trailingZeroes(self, n):
        if n < 0:
            return -1

        count = 0
        while n > 0:
            count += int(n / 5)
            n /= 5

        return count


# 11!=11*10*9*8*7*6*5*4*3*2*1
# 11!=11*(5*2)*9*(4*2)*7*(3*2)*5*(2*2)*3*(1*2)*1
# 2个5，然后再随便挑来2个2，组成2个10。其余的你们随便玩，恒不能组成乘为0结尾的
s = Solution()
print(s.trailingZeroes(11))
