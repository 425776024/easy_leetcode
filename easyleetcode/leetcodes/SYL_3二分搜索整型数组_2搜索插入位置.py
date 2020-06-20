class Solution:
    def searchInsert(self, A, targ):
        start = 0
        end = len(A) - 1
        # 不+1可能死循环
        while start + 1 < end:
            mid = int((start + end) / 2)
            if A[mid] == targ:
                return mid
            elif A[mid] < targ:
                start = mid
            else:
                end = mid
        # 此时已经确定不存在A里面了
        if A[start] > targ:  # 比start小
            return start
        elif A[end] > targ:  # 比end小
            return end
        else:
            return len(A)  # 比end大


'''
排序的数组，搜索插入的位置，用二分搜索
'''

s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))
print(s.searchInsert([1, 3, 5, 6], 0))
