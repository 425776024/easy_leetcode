

class Solution:
    def majorityElement(self, nums):
        if nums == None or len(nums) == 0:
            return -1
        key = -1
        count = 0
        for num in nums:
            if count == 0:
                key = num
                count = 1
                continue

            if key == num:
                count += 1
            else:
                count -= 1
        return key


s = Solution()
print(s.majorityElement([1, 1, 3, 2, 2, 1, 1]))
