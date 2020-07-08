class Solution(object):
    def singleNumber(self, nums):

        if nums is None:
            return 0

        result = 0
        for i in xrange(32):
            bit_i_sum = 0
            for num in nums:
                bit_i_sum += ((num >> i) & 1)
            result |= ((bit_i_sum % 3) << i)
        return result

'''
按位或
10 | 20 -> 30
bin(10):  1010
bin(20):10100
bin(30):11110
'''
s = Solution()
# 负数可以先变成正数
print(s.singleNumber([1, 1, 2, 3, 3, 3, 2, 2, 4, 1]))
a = 12
a |= 8
print(a)
