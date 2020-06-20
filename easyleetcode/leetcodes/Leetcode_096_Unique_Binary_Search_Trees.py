
class Solution:
    # @paramn n: An integer
    # @return: An integer
    def numTrees(self, n):
        if n < 0:
            return -1

        count = [0] * (n + 1)
        count[0] = 1
        count[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                count[i] += count[j] * count[i - j - 1]

        return count[n]


s = Solution()
print(s.numTrees(3))
