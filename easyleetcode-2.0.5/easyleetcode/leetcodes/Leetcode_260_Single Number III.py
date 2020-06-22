
class Solution:

    def singleNumberIII(self, A):
        nums = []
        if A == None or len(A) == 0:
            return nums

        x1xorx2 = 0
        for i in A:
            x1xorx2 ^= i
        # 求一个数二进制位1的最低位。((x & (x - 1))是将二进制比特位的值为1的最低位置零，相减得到地位所在位置)
        last1Bit = x1xorx2 - (x1xorx2 & (x1xorx2 - 1))
        # 利用last1Bit可将数组的数分为两组：相应位为0，相应最低位为1，x1 x2一定各为一组
        single1 = 0
        single2 = 0
        for i in A:
            if last1Bit & i == 0:
                single1 ^= i
            else:
                single2 ^= i
        nums.append(single1)
        nums.append(single2)
        return nums


'''
利用了x1 ^ x2不为0的特性
如果x1 ^ x2不为0，那么x1 ^ x2的结果必然存在某一二进制位不为0（即为1）

由于除了x1和x2之外其他数都是成对出现，故与最低位的1异或时一定会抵消，
因此找到的第一个最低位的1，就是x1 x2中的某一个的
最低位的1提取出来:在这一二进制位上x1和x2必然相异（1111,1110总得不一样，不然x^y=0）


'''
s = Solution()
print(s.singleNumberIII([1, 2, 2, 3, 4, 4, 5, 3]))
