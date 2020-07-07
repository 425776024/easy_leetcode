
class Solution2:
    def permute(self, nums):
        if nums is None:
            return [[]]
        elif len(nums) <= 1:
            return [nums]

        # 必须先排序，这样变成升序，然后全排列操作，变成降序就结束。思路：每次只选一对不满足降序的反转操作
        nums.sort()

        result = []
        while True:
            result.append([] + nums)
            # 从后往前寻找索引满足 a[i] < a[i + 1], 如果此条件不满足，则说明已遍历到最后一个（[3, 2, 1]）。
            i = 0
            for i in range(len(nums) - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    break
                elif i == 0:
                    return result
            # 从后往前遍历，找到第一个比a[i]大的数a[j], 即a[i] < a[j].
            j = 0
            for j in range(len(nums) - 1, i, -1):
                if nums[i] < nums[j]:
                    break
            # 交换 nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
            # 反转i + 1 ~ n之间的元素(这些元素是从小到大的，因为最前面不满足要求的被置换了，所以要变成从大到小，以便获得所以可能的组合)
            nums[i + 1:len(nums)] = nums[len(nums) - 1:i:-1]


# [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
class Solution:

    def permute(self, nums):
        # DPS with swapping
        res = []
        if len(nums) == 0:
            return res
        self.get_permute(res, nums, 0)
        return res

    def get_permute(self, res, nums, index):
        if index == len(nums):
            res.append(list(nums))
            return
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            # 拿交换后的做permute
            self.get_permute(res, nums, index + 1)
            # 撤回交换，以备新的交换（回撤）
            nums[i], nums[index] = nums[index], nums[i]

# import itertools
# def permute(nums):
#     return list(itertools.permutations(nums))


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))
    s = Solution2()
    print(s.permute([1, 2, 3]))
