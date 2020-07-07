class Solution(object):
    
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        left = 0
        for i in range(1, len(nums)):
            if nums[left] == nums[i]:
                continue
            else:
                left += 1
                nums[left] = nums[i]
        return left + 1

print('<iframe src="//player.bilibili.com/player.html?aid=456345255&bvid=BV1P5411e7hs&cid=209616726&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')