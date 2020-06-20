

class Solution:
    def kthPrimeNumber(self, k: int):
        if k <= 0:
            return -1
        count = 0
        num = 1
        while count < k:
            num += 1
            if self.isUgly(num):
                count += 1
                # print(num)
        return num

    def isUgly(self, num):
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /= 5
        while num % 7 == 0:
            num /= 7
        return num == 1


s = Solution()
print(s.kthPrimeNumber(4))
