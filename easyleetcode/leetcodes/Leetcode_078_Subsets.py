
class Solution(object):

    def subsets(self, nums):
        # Sort and iteratively generate n subset with n-1 subset, O(n^2) and O(2^n)
        # 根据题意，最终返回结果中子集类的元素应该按照升序排列，故首先需要对原数组进行排序
        nums.sort()
        res = [[]]
        # 对数组遍历，每一轮都保存之前的结果并将其依次加入到最终返回结果中。
        for index in range(len(nums)):
            # use existing subsets to generate new subsets
            for j in range(len(res)):
                # copy list
                curr = res[j][:]
                curr.append(nums[index])
                res.append(curr)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
