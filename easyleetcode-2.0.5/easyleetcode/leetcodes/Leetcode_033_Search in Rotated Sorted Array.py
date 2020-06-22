class Solution:
    def search(self, A, target):
        if A is None:
            return -1
        start = 0
        end = len(A) - 1
        mid = 0
        while start + 1 < end:
            # 取中点
            mid = start + int((end - start) / 2)
            # 如果找到直接返回
            if target == A[mid]:
                return mid
            # 这一步很关键，可以区分mid在旋转后两段有序数组中的哪一段
            if A[start] < A[mid]:
                # 关键，显然此时target在mid左边，那么缩小区间为end = mid
                if A[start] <= target and target < A[mid]:
                    end = mid
                else:  # 显然此时target在mid右，那么缩小区间为 start = mid
                    start = mid
            else:
                # 关键
                if A[mid] < target and target <= A[end]:
                    start = mid
                else:
                    end = mid
        # 此时就剩start、end两个点有可能了
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1


# 输入旋转排序数组
# 搜索给定值的位置
s = Solution()
print(s.search([8, 9, 10, 11, 12, 13, 14, 4, 5, 6], 6))
