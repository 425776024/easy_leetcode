class Solution:

    def partitionArray(self, nums, k):
        right = 0
        size = len(nums)
        for i in range(size):
            if nums[i] < k:
                nums[i], nums[right] = nums[right], nums[i]
                right += 1

        return right, nums


# 2 用快速排序的index选择，left=0,right=size-1
class Solution2:
    def partitionArray(self, nums, k):
        left, right = 0, len(nums) - 1
        while left < right:
            # 找到左边第一个>=k的
            while left < right and nums[left] < k:
                left += 1
            # 找到右边第一个<=k的
            while right > left and nums[right] > k:
                right -= 1
            # 互换位置
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left, nums

print('<iframe src="//player.bilibili.com/player.html?aid=626257955&bvid=BV1dt4y1975P&cid=209615218&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')

s = Solution()
s2 = Solution2()
arr = [3, 2, 5, 6, 9, 1]
# 划分为大于4，小于4的两个部分
print('划分轴、划分结果：', s.partitionArray(arr, 4))
print('划分轴、划分结果：', s2.partitionArray(arr, 4))
