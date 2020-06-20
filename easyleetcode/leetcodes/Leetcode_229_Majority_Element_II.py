
class Solution:
    def majorityElement(self, nums):
        res = []
        a = 0
        b = 0
        cnt1 = 0
        cnt2 = 0
        n = len(nums)
        # 统计2个众数
        for num in nums:
            if cnt1 == 0:
                a = num
                cnt1 = 1
            elif cnt2 == 0 and a != num:
                b = num
                cnt2 = 1
            elif num == a:
                cnt1 += 1
            elif num == b:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for num in nums:
            if num == a:
                cnt1 += 1
            elif num == b:
                cnt2 += 1

        if cnt1 > n / 3:
            res.append(a)
        if cnt2 > n / 3:
            res.append(b)
        return res


s = Solution()
print(s.majorityElement([1, 2, 1, 2, 1, 3, 3]))
