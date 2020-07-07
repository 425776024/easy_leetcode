class Solution:
    def call(self, arr, elem):
        i = 0
        j = 0
        while i < len(arr):
            # 如果相当则忽略，进入下一个位置
            if arr[i] == elem:
                pass
            else:  # 如果不等，则加入新的以left为长度计算的arr
                arr[j] = arr[i]
                j += 1  # left长度加以
            i += 1  # 进入下一轮判断
        return (j, arr[0:j])

print('<iframe src="//player.bilibili.com/player.html?aid=711256885&bvid=BV15D4y1S7pg&cid=209613385&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')
s = Solution()
print(s.call([0, 4, 4, 0, 0, 2, 4, 4, 1, 2, 3, 4, 8], 4))
