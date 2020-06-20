
class Solution:
    def fib(self, N):
        if N <= 1:
            return N
        a = 0
        b = 1
        for i in range(2, N):
            sum = a + b
            a, b = b, sum
        return b


s = Solution()
print(s.fib(10))
