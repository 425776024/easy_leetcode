
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """

    def searchRange(self, A, target):
        ret = [-1, -1]
        if not A:
            return ret

        # find the first position of target
        st, ed = 0, len(A) - 1
        while st + 1 < ed:
            mid = int((st + ed) / 2)
            if A[mid] == target:
                ed = mid
            elif A[mid] < target:
                st = mid
            else:
                ed = mid
        if A[st] == target:
            ret[0] = st
        elif A[ed] == target:
            ret[0] = ed
        # find the last position of target
        st, ed = 0, len(A) - 1
        while st + 1 < ed:
            mid = int((st + ed) / 2)
            if A[mid] == target:
                st = mid
            elif A[mid] < target:
                st = mid
            else:
                ed = mid
        if A[ed] == target:
            ret[1] = ed
        elif A[st] == target:
            ret[1] = st

        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
