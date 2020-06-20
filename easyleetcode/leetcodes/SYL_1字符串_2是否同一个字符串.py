import collections


class Solution:
    def anagram(self, s, t):
        cs = collections.Counter(s)
        ct = collections.Counter(t)
        return cs == ct


class Solution2:

    def anagram(self, s, t):
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    # 字符串忽略顺序，是否为同一个
    s2 = Solution2()
    a2 = s2.anagram('abcdeee', 'eeeadcb')
    print(a2)
