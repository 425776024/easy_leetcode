

class Solution:
    def aplusb(self, a, b):
        result = a ^ b
        carry = a & b
        carry <<= 1
        if carry != 0:
            result = self.aplusb(result, carry)

        return result

    def add(self, a, b):
        # 非递归
        # 只要进位不为0。某次b=0，意味着没有进位了，加完不用改变（就是答案）
        while b != 0:
            # 忽略a+b的进位，计算a+b个位值
            temp = a ^ b
            # 计算a+b的进位
            b = (a & b) << 1
            a = temp
            # 下一轮，拿计算的进位值+个位值
        return a


s = Solution()
print(s.add(13, 34))
