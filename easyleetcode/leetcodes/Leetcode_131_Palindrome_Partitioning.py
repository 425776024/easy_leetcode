
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        result = []
        if not s:
            return result

        temp = []
        self.dfs(s, 0, temp, result)
        return result

    def dfs(self, s, pos, temp, result):
        # 直至取到最后一个位置，最后将临时列表中的子串加入到最终返回结果中
        if pos == len(s):
            # result.append(temp.copy())
            result.append(temp+[])
            return

        for i in range(pos + 1, len(s) + 1):
            # 穷举看是否是回文串
            if not self.isPalindrome(s[pos:i]):
                continue
            # 是的话，加入
            temp.append(s[pos:i])
            # 看他是否能继续组成回文串
            self.dfs(s, i, temp, result)
            # 回溯
            temp.pop()

    def isPalindrome(self, s):
        if not s:
            return False
        # reverse compare
        return s == s[::-1]


print(Solution().partition('aab'))
