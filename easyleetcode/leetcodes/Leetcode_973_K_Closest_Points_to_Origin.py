class Solution(object):

    def kClosest(self, points, K):
        # K smallest heaq
        return heapq.nsmallest(K, points, key=lambda x: x[0] ** 2 + x[1] ** 2)
