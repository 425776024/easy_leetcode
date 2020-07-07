
class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        if num is None or len(num) <= 1:
            return num
        # step1: find nums[i] < nums[i + 1], Loop backwards
        i = 0
        for i in range(len(num) - 2, -1, -1):
            if num[i] < num[i + 1]:
                break
            elif i == 0:
                # reverse nums if reach maximum
                num.reverse()
                return num
        # step2: find nums[i] < nums[j], Loop backwards
        j = 0
        for j in range(len(num) - 1, i, -1):
            if num[i] < num[j]:
                break
        # step3: swap betwenn nums[i] and nums[j]
        num[i], num[j] = num[j], num[i]
        # step4: reverse between [i + 1, n - 1]
        num[i + 1:len(num)] = num[len(num) - 1:i:-1]
        return num

print(Solution().nextPermutation([3,2,1]))
print(Solution().nextPermutation([1,2,3]))