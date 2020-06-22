class Solution(object):

    def lengthOfLongestSubstring(self, s):
        charMap = {} # S
        for i in range(256):
            charMap[i] = -1
        ls = len(s)
        i = max_len = 0
        max_str = ''
        for j in range(ls):
            # Note that when charMap[ord(s[j])] >= i, it means that there are
            # duplicate character in current i,j. So we need to update i.
            if charMap[ord(s[j])] >= i:
                i = charMap[ord(s[j])] + 1
            charMap[ord(s[j])] = j
            m_str = s[i:j+1]
            if len(m_str)>len(max_str):
                max_str = m_str
            max_len = max(max_len, j - i + 1)
        return max_len,max_str

s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))