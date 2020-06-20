
class Solution:
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        res = [0] * (n + 1)
        res[0] = 1
        return res


s = Solution()
print(s.plusOne([9, 9, 9]))
print(s.plusOne([1, 2, 9]))
