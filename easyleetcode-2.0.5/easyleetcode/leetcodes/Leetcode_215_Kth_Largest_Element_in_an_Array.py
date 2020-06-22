
class Solution:
    def call(self, nums, k):
        if nums == None or len(nums) == 0:
            return -1
        result = self.qsort(nums, 0, len(nums) - 1, k)
        return result

    def qsort(self, nums, L, u, k):
        '''
        快排的一次快排操作函数
        :param nums:
        :param L: 左边
        :param u: 右边
        :param k: 第k大
        :return:
        '''
        if L >= u:
            return nums[u]

        m = L
        for i in range(L + 1, u + 1):  # u + 1保证遍历到u位置的值
            # 以nums[L]为基准，只要m右边的比它大就转到m左边
            if nums[i] > nums[L]:
                m += 1
                nums[m], nums[i] = nums[i], nums[m]
        # 此时，m左边的比nums[m]大，右边的比nums[m]小
        nums[m], nums[L] = nums[L], nums[m]
        # m左边有m-1个数，nums[m]是第m+1大（1开始）
        if m + 1 == k:
            return nums[m]
        elif m + 1 > k:  # 左边大于k-1个数时，第k大在左边
            return self.qsort(nums, L, m - 1, k)
        else:  # 小于k时，第k大在右边
            return self.qsort(nums, m + 1, u, k)


s = Solution()
print(s.call([6, 7, 9, 3, 2, 4, 8], 4))
