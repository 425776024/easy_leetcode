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
                return True, mid
            # 这一步很关键，可以区分mid在旋转后两段有序数组中的哪一段
            if A[start] < A[mid]:
                # 关键，显然此时target在mid左边，那么缩小区间为end = mid
                if A[start] <= target and target < A[mid]:
                    end = mid
                else:  # 显然此时target在mid右，那么缩小区间为 start = mid
                    start = mid
            elif A[start] > A[mid]:
                # 关键
                if A[mid] < target and target <= A[end]:
                    start = mid
                else:
                    end = mid
            # 此时A[start] =A[mid] ，需要慢慢移动缩小范围
            else:
                # 或者end-=1
                start += 1
        # 此时就剩start、end两个点有可能了
        if A[start] == target:
            return True, start
        if A[end] == target:
            return True, end
        return False, -1


# 从小到大的数组被旋转
# 二分搜索，穷举旋转的时候，mid坐在左、右边情况
# 考虑start mid  值相同的时候

s = Solution()
print(s.search([3, 4, 4, 5, 7, 0, 1, 2], 4))
