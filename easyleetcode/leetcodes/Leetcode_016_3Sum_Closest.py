
class Solution:
    '''
    找到数组中结果与k接近的3个元素
    '''

    def threeSumClosest(self, numbers, target):
        # 排序
        numbers.sort()
        # 最接近的和
        ans = None
        # 结果列表
        res = []
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1

            while left < right:
                sum = numbers[left] + numbers[i] + numbers[right]
                # 比较最近和
                if ans is None or abs(sum - target) < abs(ans - target):
                    ans = sum
                    res = [numbers[i], numbers[left], numbers[right]]
                # 因为已经从小到大排序
                if sum <= target:  # 小于target时尝试左边变得更大
                    left += 1
                else:  # 大于target时尝试右边变得更小
                    right -= 1
        return ans, res

print('<iframe src="//player.bilibili.com/player.html?aid=626255894&bvid=BV19t4y197WW&cid=209616540&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')

s = Solution()
print(s.threeSumClosest([-1, 1, 2, -4, -1], 1))
