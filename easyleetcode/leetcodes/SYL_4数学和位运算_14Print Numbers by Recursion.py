
import math


class Solution:
    def numbersByRecursion(self, n):
        result = []
        if n <= 0:
            return result
        self.helper(n, result)
        return result

    def helper(self, n, ret):
        if n == 0:
            return
        self.helper(n - 1, ret)
        # 10, 20, 30...
        base = 10**(n - 1)
        # 0,9,99,999
        size = len(ret)
        print('size:',size)

        for i in range(1, 10):
            # // add 10, 100, 1000...
            ret.append(i * base)
            for j in range(0, size):
                # // add 11, 12, 13...
                ret.append(ret[j] + base * i)


s = Solution()
print(s.numbersByRecursion(2))
