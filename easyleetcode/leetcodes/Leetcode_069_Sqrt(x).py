class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x < 0:
            return -1
        elif x == 0:
            return 0

        start, end = 1, x
        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid ** 2 == x:
                return mid
            # mid此时过大，那真实值在mid左边，所以end=mid逼近
            elif mid ** 2 > x:
                end = mid
            else:  # mid此时小于目标，那么真实在右边，所以start逼近
                start = mid
        return start


s = Solution()
print(s.mySqrt(9))
