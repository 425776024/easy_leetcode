class Solution(object):

    def minDistance(self, word1, word2):
        ls_1, ls_2 = len(word1), len(word2)
        dp = range(ls_1 + 1)
        for j in range(1, ls_2 + 1):
            pre = dp[0]
            dp[0] = j
            for i in range(1, ls_1 + 1):
                temp = dp[i]
                if word1[i - 1] == word2[j - 1]:
                    dp[i] = pre
                else:
                    dp[i] = min(pre + 1, dp[i] + 1, dp[i - 1] + 1)
                pre = temp
        return dp[ls_1]
