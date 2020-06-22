

class Solution:
    def call(self, nums, target):
        '''
        在nums中找到两个数，满足和为target
        :param nums:
        :param target:
        :return:
        '''
        hashset = {}
        res = []
        for i, m in enumerate(nums):
            if target - m not in hashset:
                hashset[m] = i
            else:
                res.append([hashset[target - m], i])
        return res

    def call2(self, nums, k):
        '''
        在nums中找到3个数，满足和为k
        :param nums:
        :param k:
        :return:
        '''
        if len(nums) < 3:
            return nums
        result = []
        for i in range(len(nums) - 1):
            target = k - nums[i]
            # 避免重复，从后面的数组开始寻找（如果中间某个有和前面相加为目标值的，那么，在前面步骤的时候也能计算发现）
            s = self.call(nums[i + 1:], target)
            if len(s) != 0:
                for p in s:
                    # ss = [nums[i], nums[i + p[0] + 1], nums[i + p[1] + 1]]
                    ss = [i, i + 1 + p[0], i + 1 + p[1]]
                    if ss not in result:
                        result.append(ss)
        return result


s = Solution()
print(s.call2([-1, 0, 1, 2, -1, -4], -1))
