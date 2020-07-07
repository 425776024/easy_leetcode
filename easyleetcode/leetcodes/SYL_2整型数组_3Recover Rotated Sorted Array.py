class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if nums == None:
            return
        numslen = len(nums)
        # 第首数，比最后数大：从小到大排序
        if nums[0] > nums[-1]:
            for index in range(numslen - 1):
                # 找到旋转的那个点
                # 从小到大排序：旋转点前一位比后一位 大
                if nums[index] > nums[index + 1]:
                    self.reverse(nums, 0, index)
                    self.reverse(nums, index + 1, numslen - 1)
                    self.reverse(nums, 0, numslen - 1)
        else:
            # 第首数，比最后数小：从大到小排序
            for index in range(numslen - 1):
                # 找到旋转的那个点
                # 从大到小排序：旋转点前一位比后一位 小
                if nums[index] < nums[index + 1]:
                    self.reverse(nums, 0, index)
                    self.reverse(nums, index + 1, numslen - 1)
                    self.reverse(nums, 0, numslen - 1)

    def reverse(self, nums, start, end):
        # 无条件反转
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

print('<iframe src="//player.bilibili.com/player.html?aid=498781832&bvid=BV1jK411H7LN&cid=209614077&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')

s = Solution()
# 小到大排序
# [5,4] [3,2,1]
# [1,2,3,4,5]
nums = [4, 5, 1, 2, 3]
s.recoverRotatedSortedArray(nums)
print(nums)
# 大到小排序
# [1,2] [3,4,5]
# [5,4,3,2,1]
nums = [2, 1, 5, 4, 3]
s.recoverRotatedSortedArray(nums)
print(nums)
