'''
# 1 两个for循环穷举
class Solution:
    def call(self, arr, sum_obj_elem, once=True):
        size = len(arr)
        result = []
        for i1 in range(size):
            sum=0
            for i2 in range(i1, size):
                sum += arr[i2]
                if sum == sum_obj_elem:
                    # print(i1, i2)
                    result.append([i1, i2])
                    if once:
                        return result
        return result


s = Solution()
print(s.call([-3, 1, 2, -3, 4], 3, False))
'''


# 分奇偶对讨论，奇：按中轴划分-3, 1, 2。偶：按左右划分1, 6, 2, -1, -2, -6
# 一句话总结：xxxxx子串和为0，只存在奇/偶两个个数情况，所有列举两种情况时从中间展开计算和是否为零即可（奇：1 1 1, 2, -1 -1 -3;偶:1 2 , -1 -2）
class Solution2:
    def call(self, arr, sum_obj_elem, once=True):
        size = len(arr)
        result = []
        if arr[0] == sum_obj_elem:
            result.append(0)
            result.append(0)
            return result
        for center in range(size):
            if once and len(result) > 0:
                break

            # 奇数形式
            left_len = center
            right_len = size - 1 - center
            d = min(left_len, right_len)
            # print(left_len, right_len)
            sum = 0
            left = center
            right = center
            sum += arr[center]
            while d > 0 and left - 1 >= 0 and right + 1 < size:
                d -= 1
                left -= 1
                right += 1
                sum += arr[left]
                sum += arr[right]
                if sum == sum_obj_elem:
                    result.append([left, right])
                    # result.append(arr[left:right + 1])
                    break

            #  计算偶数对形式，此时没有center
            left_len = center + 1
            right_len = size - 1 - center
            d = min(left_len, right_len)
            left = center
            right = center + 1
            sum = 0
            # 注意，和奇的时候-= 1,+= 1位置不一样，奇的时候左右轴一个位置，得先加中轴：sum += arr[center]，然后+-。偶的时候，得先sum+=，然后left、right移位
            while d > 0 and left >= 0 and right < size:
                d -= 1
                sum += arr[left]
                sum += arr[right]
                if sum == sum_obj_elem:
                    # result.append(arr[left:right + 1])
                    result.append([left, right])
                    break
                left -= 1
                right += 1

        return result

print('<iframe src="//player.bilibili.com/player.html?aid=711373357&bvid=BV1cD4y1D7Zg&cid=209613537&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>')

s = Solution2()
print(s.call([5, -3, 1, 3, -3, -1, 1, 6, 2, -1, -2, -6], 0, False))
