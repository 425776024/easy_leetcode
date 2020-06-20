


class Solution(object):
    def singleNumber(self, nums):
        if nums is None:
            return 0

        result = 0
        for i in range(32):
            # 统计第i位上1出现的个数
            bit_i_sum = 0
            for num in nums:
                # &1：是否是1/0。num/(2**i)
                bit_i_sum += ((num >> i) & 1)
            # i位上整数出现了三次，对3取余为0。如果有落单会满足超高3，此时次i位置会有1，还原成int
            c = ((bit_i_sum % 3) << i)
            # 当前i位的二进制累加和
            result |= c
        return self.twos_comp(result, 32)

    def twos_comp(self, val, bits):
        # (1 << (bits - 1)):1*(2**31)
        '''
        很容易想到，可以将一个二进制位（bit）专门规定为符号位，它等于0时就表示正数，等于1时就表示负数。
        比如，在8位机中，规定每个字节的最高位为符号位。那么，+8就是00001000，而-8则是10001000。
        但是，随便找一本《计算机原理》，都会告诉你，实际上，计算机内部采用2的补码（Two's Complement）表示负数
        '''
        d = -(val & (1 << (bits - 1))) | (val & ((1 << (bits - 1)) - 1))
        print(-2147483648 | 2147483644)
        return d


s = Solution()
print(s.singleNumber([1, 1, 2, 3, 3, 3, 2, 2, -4, 1]))
a = 12

a |= 8
print(a)
