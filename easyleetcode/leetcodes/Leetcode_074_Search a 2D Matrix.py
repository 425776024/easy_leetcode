class Solution:
    '''
    一次二分搜索，把矩阵当数组看
    '''

    def search_matrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        # 横，纵
        m, n = len(matrix), len(matrix[0])
        # 把矩阵当数组！
        st, ed = 0, m * n - 1
        while st + 1 < ed:
            mid = int((st + ed) / 2)
            # int(mid / n)取得1维索引，mid % n取得2维索引
            v = matrix[int(mid / n)][mid % n]
            if v == target:
                return True, [int(mid / n), mid % n]
            elif v < target:
                st = mid
            else:
                ed = mid
        if matrix[int(st / n)][st % n] == target:
            return True, [int(st / n), st % n]
        elif matrix[int(ed / n)][ed % n] == target:
            return True, [int(ed / n), ed % n]
        return False, [-1, -1]


n = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]

s = Solution()
print(s.search_matrix(n, 16))

