'''
二分搜索
'''


class Solution:
    def findMedianSortedArrays(self, A, B):
        n = len(A) + len(B)
        # 奇数情况直接有
        if n % 2 == 1:
            return self.findKth(A, B, int(n / 2) + 1)
        else:  # 偶数情况返回中间数
            smaller = self.findKth(A, B, int(n / 2))
            bigger = self.findKth(A, B, int(n / 2) + 1)
            return (smaller + bigger) / 2.0

    def findKth(self, A, B, k):
        # 从排序数组A、B中找第k大的数
        # 此时A空，找第k个数，那么就是B中的k-1号了，因为都是排序了的
        if len(A) == 0:
            return B[k - 1]
        # B空，第k大个数，那就是A第k-1号
        if len(B) == 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
        # 如果A拥有k/2以上的数，找到第k/2个数
        a = A[int(k / 2) - 1] if len(A) >= int(k / 2) else None
        # 如果B拥有k/2以上的数，找到第k/2个数
        b = B[int(k / 2) - 1] if len(B) >= int(k / 2) else None

        # （无有）B中没有k/2以上数据，（则A中一定超过k/2）,此时第k大一定：不在A的前k/2
        # （有有a<b）B有k/2以上，如果A有k/2以上且a<b。则第k大一定：不在A的前k/2
        if b is None or (a is not None and a < b):
            return self.findKth(A[int(k / 2):], B, k - int(k / 2))
        # （无无 x）
        # （有无）B中有k/2以上数据，但A小于k/2数据：不在B的前k/2
        # （有有a>b）B中有k/2以上数据，A有k/2以上数据，A第k/2个数据比B的第k/2大：不在B的前k/2
        return self.findKth(A, B[int(k / 2):], k - int(k / 2))


'''
借用findKthNumber的思想。先实现findKthNumber，如果是偶数个，则把中间2个加起来平均，奇数就用中间的。
可以泛化为一般的找第 k 大数
'''

A = [1, 2, 3, 4, 5, 6]
B = [2, 3, 4, 5]
s = Solution()
print(s.findMedianSortedArrays(A, B))
