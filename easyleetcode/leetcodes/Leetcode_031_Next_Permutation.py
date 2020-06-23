class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ls = len(nums)
        if ls <= 1:
            return
        pair = []
        for i in range(ls):
            for j in range(i + 1, ls):
                # append ascending order pair
                if nums[i] < nums[j]:
                    pair.append([i,j])
        pos = 0
        if len(pair) > 0:
            self.swap(nums, pair[-1][0], pair[-1][1])
            pos = pair[-1][0] + 1
        # sort from pos
        for i in range(pos, ls):
            for j in range(i + 1, ls):
                if nums[i] > nums[j]:
                    self.swap(nums, i, j)

    def swap(self, nums, index1, index2):
        if index1 == index2:
            return
        nums[index1], nums[index2] = nums[index2], nums[index1]

    