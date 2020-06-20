import collections


class Solution:
    def compare_strings(self, A, B):
        tp = collections.defaultdict(int)
        for a in A:
            tp[a] += 1
        for b in B:
            if b not in tp:
                return False
            elif tp[b] <= 0:
                return False
            else:
                tp[b] -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    # absje是否是aabbshdjee的子集
    a = s.compare_strings('aabbshdjee', 'absje')
    print(a)
