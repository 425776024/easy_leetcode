class Solution(object):


    def maxSubArray(self, nums):
        maxEndingHere = maxSofFar = nums[0]
        for i in range(1, len(nums)):
            maxEndingHere = max(maxEndingHere + nums[i], nums[i])
            maxSofFar = max(maxEndingHere, maxSofFar)
        return maxSofFar