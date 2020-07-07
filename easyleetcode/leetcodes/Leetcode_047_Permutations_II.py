class Solution:
    def permuteUnique(self, nums):
        nums.sort()  # 数组先排序
        self.res = []
        self.recur(nums, [])
        return self.res

    def recur(self, nums, temp):
        # 对nums进行全排列，结果保存至temp
        if nums == []:
            # 对空进行全排列，结果保存至temp，意味着排完了，可以保存结果
            self.res.append(temp)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # 每当进入新的构成，先考虑该构成的首字符是否和上一个一样。
                continue

            # 第i号nums[i]放入结果（temp)中， 不用进行全排列，只对除i号以外的全排列
            self.recur(nums[:i] + nums[i + 1:], temp + [nums[i]])


if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1, 2, 2]))
