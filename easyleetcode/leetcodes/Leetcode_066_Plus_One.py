class Solution:
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n - 1, -1, -1):
            # 个位不进位，则返回
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # 进位则这里必须是0（plus one)
            digits[i] = 0
        # 能到这一步，一定进位了，最前面一定是1
        res = [0] * (n + 1)
        res[0] = 1
        return res


s = Solution()
print(s.plusOne([9, 9, 9]))
print(s.plusOne([1, 2, 9]))
