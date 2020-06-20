


class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            # 如果 nums[i] 在正常数组范围，且没有在正确的桶排序位置（值为多少在多少号）
            while nums[i] > 0 and nums[i] <= n and nums[i] != i + 1:
                # 这样写出错 nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i],因为后面那个需要用到nums[i]
                # 把值为nums[i] - 1的放入nums[i] 位置，（桶排序应该的位置，值为1放入0号桶序号）
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # 从0开始遍历，看那个数子不与其桶序号对应（0号位置对应值1）
        # 原数组：[3, 4, -1, 1]；此时数组是：[1,-1,3,4]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1


s = Solution()
# [3, 4, -1, 1]
# [-1, 4, 3, 1]
# [-1, 1, 3, 4]
# [-1, 1, 3, 4]
# [1, -1, 3, 4]
print(s.firstMissingPositive([3, 4, -1, 1]))
print(s.firstMissingPositive([7, 8, 9, 11, 12]))
