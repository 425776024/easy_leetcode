
from copy import deepcopy


class Solution:
    def majorityNumber(self, nums, k):
        if nums == None:
            return 0
        d = {}
        majority = 0
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
            if d[num] * k > len(nums):
                majority = num
                break
            if len(d) >= k:
                self.clean(d)
        return majority

    def clean(self, d: dict):
        max_v = 0
        for v in d.values():
            if v > max_v:
                max_v = v
        remove_ids = []
        for k in d.keys():
            if d[k] < max_v:
                remove_ids.append(k)
        for rid in remove_ids:
            del d[rid]


s = Solution()
print(s.majorityNumber([3, 1, 2, 3, 2, 3, 3, 4, 4, 4], k=3))
