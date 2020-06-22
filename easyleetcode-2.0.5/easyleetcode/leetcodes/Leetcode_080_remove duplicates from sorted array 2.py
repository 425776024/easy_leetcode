
class Solution:
    def call(self, nums, dupsize=2):
        j = 0  # 新的满足要求的数组索引
        i = 0  # 用于遍历
        count = 1
        while i < len(nums):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                count += 1
            else:
                # 插入j为末尾的新标记数组
                d = min(count, dupsize)
                for k in range(d):
                    nums[j] = nums[i]
                    j += 1
                # 新的起点
                count = 1
            # 进入新的判断的索引
            i += 1

        return nums[:j]


s = Solution()
print(s.call([1, 1, 1, 1, 1, 4, 4, 2, 2, 2, 3], 3))
