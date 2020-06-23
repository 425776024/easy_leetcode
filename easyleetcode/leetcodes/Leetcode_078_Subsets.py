class Solution(object):


    def subsets(self, nums):
        # Sort and iteratively generate n subset with n-1 subset, O(n^2) and O(2^n)
        nums.sort()
        res = [[]]
        for index in range(len(nums)):
            size = len(res)
            # use existing subsets to generate new subsets
            for j in range(size):
                curr = list(res[j])
                curr.append(nums[index])
                res.append(curr)
        return res




if __name__ == "__main__":
    s = Solution()
    print s.subsets([1,2,3])
