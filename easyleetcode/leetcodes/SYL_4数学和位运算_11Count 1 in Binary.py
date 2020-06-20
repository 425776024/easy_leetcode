
class Solution:
    def countOnes(self, num):
        count = 0
        while num:
            print(bin(num))
            # num = (num - 1) & num
            num &= num - 1
            count += 1

        return count


s = Solution()
print(s.countOnes(1023))
