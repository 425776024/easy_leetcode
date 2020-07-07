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

print('<iframe src="//player.bilibili.com/player.html?aid=841169118&bvid=BV1E54y1z7DX&cid=208094419&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')
if __name__ == '__main__':
    s = Solution()
    # absje是否是aabbshdjee的子集
    a = s.compare_strings('aabbshdjee', 'absje')
    print(a)
