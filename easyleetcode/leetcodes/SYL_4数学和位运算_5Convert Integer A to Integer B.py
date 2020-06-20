


class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """

    def bitSwapRequired(self, a, b):
        count = 0
        # 相同的位上为0，不同的位上为1，故接下来只需将异或后1的个数求出即可
        a_xor_b = a ^ b
        neg_flag = False
        if a_xor_b < 0:
            a_xor_b = abs(a_xor_b) - 1
            neg_flag = True
        while a_xor_b > 0:
            count += 1
            # x & (x - 1)：将二进制比特位的值为1的最低位置零
            a_xor_b = a_xor_b & (a_xor_b - 1)

        # bit_wise = 32
        if neg_flag:
            # Python时需要对负数专门处理，转换为求其补数中0的个数。
            count = 32 - count
        return count


'''
返回两个数字，二进制的1差
使用异或处理两个整数，相同的位上为0，不同的位上为1，故接下来只需将异或后1的个数求出即可
'''

s = Solution()
print(s.bitSwapRequired(31, 14))
