

class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        res = [[]]
        begin = 0
        for index in range(len(nums)):
            # 如果不是（和前一位）重复，就和之前一样从0开始生成
            # 否则，只从前一位生成的元素开始
            if index == 0 or nums[index] != nums[index - 1]:
                # generate all
                begin = 0
            size = len(res)
            # use existing subsets to generate new subsets
            for j in range(begin, size):
                curr = list(res[j])
                curr.append(nums[index])
                res.append(curr)
            # avoid duplicate subsets
            begin = size
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))
