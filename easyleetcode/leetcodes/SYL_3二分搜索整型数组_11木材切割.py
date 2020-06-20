class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """

    def woodCut(self, L, k):
        if sum(L) < k:
            return 0

        start, end = 1, max(L)
        i = 0
        while start + 1 < end:
            i += 1
            # 木材长,这几约定为整数
            mid = int((start + end) / 2)
            print(i, mid)
            # 总共的木材
            pieces_sum = sum(int(len_i / mid) for len_i in L)
            # 比k少，说明木材长度取大了，所以end=mid进行减少逼近
            if pieces_sum < k:
                end = mid
            else:
                start = mid

        # 优先取长的试试
        if sum(int(len_i / end) for len_i in L) >= k:
            return end
        return start


'''
且最少k根木材，要求切的尽可能长
'''

s = Solution()
print(s.woodCut([232, 124, 456], k=7))
