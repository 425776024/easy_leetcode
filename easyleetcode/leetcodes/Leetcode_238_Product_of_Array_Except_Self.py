class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1] * len(nums)
        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans


print('<iframe src="//player.bilibili.com/player.html?aid=841253292&bvid=BV1N54y1q77u&cid=209614267&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')